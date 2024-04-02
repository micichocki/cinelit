import { Component } from '@angular/core';
import { MainStoreService } from '../store/main-store.service';

@Component({
  selector: 'app-stats',
  standalone: true,
  imports: [],
  templateUrl: './stats.component.html',
  styleUrl: './stats.component.scss'
})
export class StatsComponent {
  constructor(private store: MainStoreService) {}

  ngOnInit() {
    this.store.setCurrentSubpage('Stats');
  }
}
