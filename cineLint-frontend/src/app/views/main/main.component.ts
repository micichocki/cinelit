import { ChangeDetectorRef, Component, OnInit } from "@angular/core";
import { RouterLink, RouterOutlet } from "@angular/router";
import { MatIconModule } from "@angular/material/icon";
import { MatToolbarModule } from "@angular/material/toolbar";
import { MainStoreService, SubpageType } from "./store/main-store.service";
import { CommonModule } from "@angular/common";

@Component({
  selector: "app-main",
  standalone: true,
  imports: [
    RouterOutlet,
    RouterLink,
    MatIconModule,
    MatToolbarModule,
    CommonModule,
  ],
  templateUrl: "./main.component.html",
  styleUrl: "./main.component.scss",
})
export class MainComponent implements OnInit {
  protected subpages = [
    {
      name: "Home",
      icon: "home",
      routerLink: "/home",
    },
    {
      name: "Collection",
      icon: "view_list",
      routerLink: "/collection",
    },
    {
      name: "Stats",
      icon: "bar_chart",
      routerLink: "/stats",
    },
  ];

  protected currentSubpage: SubpageType | null = null;

  constructor(
    private store: MainStoreService,
    private cdr: ChangeDetectorRef
  ) {}

  ngOnInit() {
    this.store.currentSubpage$.subscribe((subpage) => {
      this.currentSubpage = subpage;
      this.cdr.detectChanges();
    });
  }

  changeSubpage(subpage: SubpageType) {
    this.store.setCurrentSubpage(subpage);
  }
}
