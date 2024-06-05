import { Component } from "@angular/core";
import { MainStoreService } from "../store/main-store.service";
import { MatGridListModule } from "@angular/material/grid-list";
import { MatCardModule } from "@angular/material/card";
import { BreakpointObserver, Breakpoints } from "@angular/cdk/layout";
import { FlexLayoutModule } from "@angular/flex-layout";
import { MatProgressBarModule } from "@angular/material/progress-bar";
import { MatIconModule } from "@angular/material/icon";
import { MatDividerModule } from "@angular/material/divider";
import { MatButtonModule } from "@angular/material/button";
import { ActivatedRoute, Router, RouterLink } from "@angular/router";
import { RepositoryService } from "src/app/shared/services/repository.service";
import { mergeMap } from "rxjs";
import { CommonModule } from "@angular/common";
import { AuthService } from "src/app/shared/services/auth.service";

@Component({
  selector: "app-current",
  standalone: true,
  imports: [
    MatGridListModule,
    MatCardModule,
    FlexLayoutModule,
    MatProgressBarModule,
    MatButtonModule,
    MatDividerModule,
    MatIconModule,
    RouterLink,
    CommonModule,
  ],
  templateUrl: "./current.component.html",
  styleUrl: "./current.component.scss",
})
export class CurrentComponent {
  item: any;
  mode = "Book";
  sessions: any;
  isSmallScreen = false;
  overallReadPages: number = 0;
  overallReadingTime: number = 0;
  readingSpeed: number = 0;
  numberOfSessions: number = 0;
  estimatedTimeToFinish: number = 0;
  totalWatchTime: number = 0;

  constructor(
    private activatedRoute: ActivatedRoute,
    private repositoryService: RepositoryService,
    private breakpointObserver: BreakpointObserver,
    private auth: AuthService
  ) {
    breakpointObserver
      .observe([Breakpoints.XSmall, Breakpoints.Tablet])
      .subscribe((result) => {
        this.isSmallScreen = result.matches;
      });
  }

  ngOnInit() {
    this.activatedRoute.queryParams
      .pipe(
        mergeMap((params) => {
          let id = params["id"];

          return this.repositoryService.getObjectById(this.auth.userId, id);
        })
      )
      .subscribe((object) => {
        this.item = object;
        this.mode = object.objectType;

        let userId = 2;
        this.repositoryService
          .getSessionsByBook(userId, object.id)
          .subscribe((sessions) => {
            this.sessions = sessions;
            console.log(sessions);
            this.overallReadPages = sessions.reduce(
              (total: any, session: any) => total + session.pages_read,
              0
            );
            this.overallReadingTime = sessions.reduce(
              (total: any, session: any) => total + session.duration,
              0
            );
            this.readingSpeed = Math.floor(
              this.overallReadPages / this.overallReadingTime
            );
            this.totalWatchTime = sessions[0].watching_time;
            this.numberOfSessions = sessions.length;
            let remainingPages = object.num_of_pages - this.overallReadPages;
            this.estimatedTimeToFinish = Math.floor(
              remainingPages / this.readingSpeed
            );
          });
      });
  }
}
