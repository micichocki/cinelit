import { Component } from '@angular/core';
import { MainStoreService } from '../store/main-store.service';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [RouterLink],
  templateUrl: './home.component.html',
  styleUrl: './home.component.scss'
})
export class HomeComponent {
  constructor(private store: MainStoreService) {}

  ngOnInit() {
    this.store.setCurrentSubpage('Home');
  }
}
