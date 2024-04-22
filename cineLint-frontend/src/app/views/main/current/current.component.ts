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
  ],
  templateUrl: "./current.component.html",
  styleUrl: "./current.component.scss",
})
export class CurrentComponent {
  isSmallScreen = false;

  constructor(
    private store: MainStoreService,
    breakpointObserver: BreakpointObserver
  ) {
    breakpointObserver
      .observe([Breakpoints.XSmall, Breakpoints.Tablet])
      .subscribe((result) => {
        this.isSmallScreen = result.matches;
      });
  }

  ngOnInit() {
    this.store.setCurrentSubpage("Current");
  }
}
