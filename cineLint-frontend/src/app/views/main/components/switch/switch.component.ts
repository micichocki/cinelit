import { Component } from "@angular/core";
import {
  MatSlideToggleChange,
  MatSlideToggleModule,
} from "@angular/material/slide-toggle";
import { MainStoreService } from "../../store/main-store.service";
import { MatIcon } from "@angular/material/icon";

@Component({
  selector: "app-switch",
  standalone: true,
  imports: [MatSlideToggleModule, MatIcon],
  templateUrl: "./switch.component.html",
  styleUrl: "./switch.component.scss",
})
export class SwitchComponent {
  get value() {
    return this.store.mode === "Movies";
  }

  constructor(private store: MainStoreService) {}

  changeMode(event: MatSlideToggleChange) {
    if (event.checked) {
      this.store.setMode("Movies");
    } else {
      this.store.setMode("Books");
    }
  }
}
