import { Component, EventEmitter, Input, Output } from '@angular/core';

@Component({
  selector: 'app-timer',
  standalone: true,
  imports: [],
  templateUrl: './timer.component.html',
  styleUrl: './timer.component.scss'
})
export class TimerComponent {
  @Input() initialValue: number = 0;
  @Output() timerTick: EventEmitter<number> = new EventEmitter<number>();

  private intervalId!: any;
  protected time!: number;

  get value() {
    return this.time;
  }

  ngOnInit(): void {
    this.reset();
  }

  start(): void {
    this.intervalId = setInterval(() => {
      this.time = this.time + 1;
      this.timerTick.emit(this.time);
    }, 1000);
  }

  stop(): void {
    clearInterval(this.intervalId);
  }

  reset(): void {
    this.time = this.initialValue * 60;
    this.timerTick.emit(this.time);
    this.stop();
  }

  transform(value: number): string {
    const hours: number = Math.floor(value / 60 / 60);
    const minutes: number = Math.floor(value / 60);
    const seconds: number = value % 60;
    return `${hours.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
  }
}
