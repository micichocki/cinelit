import { Component } from '@angular/core';
import { MainStoreService } from '../store/main-store.service';
import { ButtonComponent } from 'src/app/shared/components/button/button.component';
import { AuthService } from 'src/app/shared/services/auth.service';

@Component({
  selector: 'app-settings',
  standalone: true,
  imports: [ButtonComponent],
  templateUrl: './settings.component.html',
  styleUrl: './settings.component.scss'
})
export class SettingsComponent {
  constructor(private store: MainStoreService, private authService: AuthService) {}

  ngOnInit() {
    this.store.setCurrentSubpage('Settings');
  }

  logout() {
    this.authService.logout();
  }

  deleteAccount() {
    this.authService.deleteAccount();
  }
}
