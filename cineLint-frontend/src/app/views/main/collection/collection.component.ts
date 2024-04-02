import { Component } from '@angular/core';
import { MainStoreService } from '../store/main-store.service';

@Component({
  selector: 'app-collection',
  standalone: true,
  imports: [],
  templateUrl: './collection.component.html',
  styleUrl: './collection.component.scss'
})
export class CollectionComponent {
  constructor(private store: MainStoreService) {}

  ngOnInit() {
    this.store.setCurrentSubpage('Collection');
  }
}
