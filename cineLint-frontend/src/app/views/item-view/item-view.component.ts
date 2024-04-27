import { CommonModule } from '@angular/common';
import { Component, HostBinding } from '@angular/core';
import { RouterLink, RouterOutlet } from '@angular/router';

@Component({
  selector: 'app-item-view',
  standalone: true,
  imports: [RouterOutlet, RouterLink, CommonModule],
  templateUrl: './item-view.component.html',
  styleUrl: './item-view.component.scss'
})
export class ItemViewComponent {
  @HostBinding('className') componentClass: string;

  constructor() {
    this.componentClass = 'background-filter book-background';
  }
}
