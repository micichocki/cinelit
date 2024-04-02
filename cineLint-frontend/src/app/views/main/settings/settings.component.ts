import { Component } from '@angular/core';
import { MainStoreService } from '../store/main-store.service';

@Component({
  selector: 'app-settings',
  standalone: true,
  imports: [],
  templateUrl: './settings.component.html',
  styleUrl: './settings.component.scss'
})
export class SettingsComponent {
  constructor(private store: MainStoreService) {}

  ngOnInit() {
    this.store.setCurrentSubpage('Settings');
  }
}
