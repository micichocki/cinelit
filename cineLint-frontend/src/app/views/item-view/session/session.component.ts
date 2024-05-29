import { Component, OnInit, ViewChild } from '@angular/core';
import { FormControl } from '@angular/forms';
import { ActivatedRoute, Router, RouterLink } from '@angular/router';
import { mergeMap } from 'rxjs';
import { ButtonComponent } from 'src/app/shared/components/button/button.component';
import { InputComponent } from 'src/app/shared/components/input/input.component';
import { TimerComponent } from 'src/app/shared/components/timer/timer.component';
import { AuthService } from 'src/app/shared/services/auth.service';
import { Book, Movie, RepositoryService, Session } from 'src/app/shared/services/repository.service';

@Component({
  selector: 'app-session',
  standalone: true,
  imports: [ButtonComponent, InputComponent, TimerComponent, RouterLink],
  templateUrl: './session.component.html',
  styleUrl: './session.component.scss'
})
export class SessionComponent implements OnInit {
  @ViewChild('timer') timer!: TimerComponent;
  item!: Book | Movie | any;
  sessionActive = false;
  pagesRead = new FormControl<number>(0);
  timestamp = new FormControl<number>(0);
  mode = 'Book';
  showConfirm = false;
  startDate: Date | null = null;
  endDate: Date | null = null;


  get continueTitle() {
    return this.sessionActive ? 'Pause' : 'Continue'
  }

  constructor(
    private activatedRoute: ActivatedRoute,
    private repositoryService: RepositoryService,
    private router: Router,
    private auth: AuthService
  ) {}

  ngOnInit() {
    this.activatedRoute.queryParams.pipe(
      mergeMap((params) => {
        let id = params['id'];

        return this.repositoryService.getObjectById(this.auth.userId, id)
      })
    ).subscribe((object: any) => {
      this.item = object;
      this.mode = object.num_of_pages ? 'Book' : 'Movie';
    });
  }

  onContinueClick() {
    if (!this.startDate) this.startDate = new Date();

    if (this.sessionActive) {
      this.timer.stop();
    }
    else {
      this.timer.start();
    }
    this.sessionActive = !this.sessionActive;
  }

  onStopClick() {
    this.timer.stop();
    this.showConfirm = true;
    this.sessionActive = false;
  }

  saveSession() {
    this.endDate = new Date();

    const session: Session = {
      item_id: this.item.id as number,
      start_date: this.startDate!.toISOString(),
      end_date: this.endDate!.toISOString(),
      duration: this.mode === 'Book' ? Math.ceil(this.timer.value / 60) : 0,
      pages_read: this.pagesRead.value as number,
      watching_time: this.mode === 'Movie' ? Math.ceil(this.timer.value / 60) : 0
    }

    this.repositoryService.saveSession(this.auth.userId, session).subscribe(() => this.router.navigate(['/home']));
  }
}
