import { CommonModule } from '@angular/common';
import { Component, Input } from '@angular/core';
import { FormControl, FormsModule, ReactiveFormsModule } from '@angular/forms';

@Component({
  selector: 'app-input',
  standalone: true,
  imports: [FormsModule, ReactiveFormsModule, CommonModule],
  templateUrl: './input.component.html',
  styleUrl: './input.component.scss'
})
export class InputComponent {
  @Input() title: string = '';
  @Input() placeholder: string = '';
  @Input() type: string = 'text';
  @Input() value: any = '';
  @Input() control: any = new FormControl(this.value);

  constructor() { }

  ngOnInit(): void {
  }
}
