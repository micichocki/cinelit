import { CommonModule } from '@angular/common';
import { Component, EventEmitter, Input, Output } from '@angular/core';

@Component({
  selector: 'app-button',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './button.component.html',
  styleUrl: './button.component.scss'
})
export class ButtonComponent {
  @Input() title: string = '';
  @Input() icon: string = '';
  @Input() size: 'small' | 'medium' | 'big' = 'medium';
  @Input() iconButton = false;
  @Input() style = 'default';
  @Input() disabled = false;
  @Input() type = 'primary';
  @Output() outClick = new EventEmitter(); 
}
