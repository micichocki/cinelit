import { Component, OnInit, ViewChild } from '@angular/core';
import { FormControl } from '@angular/forms';
import { ActivatedRoute, Router, RouterLink } from '@angular/router';
import { mergeMap } from 'rxjs';
import { ButtonComponent } from 'src/app/shared/components/button/button.component';
import { InputComponent } from 'src/app/shared/components/input/input.component';
import { TimerComponent } from 'src/app/shared/components/timer/timer.component';
import { RepositoryService } from 'src/app/shared/services/repository.service';

@Component({
  selector: 'app-session',
  standalone: true,
  imports: [ButtonComponent, InputComponent, TimerComponent, RouterLink],
  templateUrl: './session.component.html',
  styleUrl: './session.component.scss'
})
export class SessionComponent implements OnInit {
  @ViewChild('timer') timer!: TimerComponent;
  item!: any;
  sessionActive = false;
  pagesRead = new FormControl(0);
  timestamp = new FormControl(0);
  mode = 'Book';
  showConfirm = false;

  get continueTitle() {
    return this.sessionActive ? 'Pause' : 'Continue'
  }

  constructor(
    private activatedRoute: ActivatedRoute,
    private repositoryService: RepositoryService,
    private router: Router
  ) {}

  ngOnInit() {
    this.activatedRoute.queryParams.pipe(
      mergeMap((params) => {
        let id = params['id'];

        return this.repositoryService.getObjectById(id)
      })
    ).subscribe(object => {
      this.item = object;
      this.mode = object.objectType;
    });
  }

  onContinueClick() {
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
    const session = {}

    this.repositoryService.saveSession(session).subscribe();
  }
}
