import { CommonModule } from '@angular/common';
import { Component, HostBinding } from '@angular/core';
import { ActivatedRoute, RouterLink, RouterOutlet } from '@angular/router';

@Component({
  selector: 'app-item-view',
  standalone: true,
  imports: [RouterOutlet, RouterLink, CommonModule],
  templateUrl: './item-view.component.html',
  styleUrl: './item-view.component.scss'
})
export class ItemViewComponent {
  @HostBinding('className') componentClass: string = 'background-filter book-background';

  constructor(
    private activatedRoute: ActivatedRoute,
  ) {
    this.activatedRoute.queryParams.subscribe(params => {
      let type = params['type'];
      const backgroundClass = type === 'book' ? 'book-background' : 'movie-background';
      this.componentClass = `background-filter ${backgroundClass}`;
    });
}

}
