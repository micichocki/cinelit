import { Component } from '@angular/core';
import { MainStoreService } from '../store/main-store.service';

@Component({
  selector: 'app-current',
  standalone: true,
  imports: [],
  templateUrl: './current.component.html',
  styleUrl: './current.component.scss'
})
export class CurrentComponent {
  constructor(private store: MainStoreService) {}

  ngOnInit() {
    this.store.setCurrentSubpage('Current');
  }
}
