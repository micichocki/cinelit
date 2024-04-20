import { Component } from '@angular/core';
import { ApplicationMode, MainStoreService } from '../store/main-store.service';
import { MatGridListModule } from '@angular/material/grid-list';
import { MatCardModule } from '@angular/material/card';
import { BreakpointObserver, Breakpoints } from '@angular/cdk/layout';
import { FlexLayoutModule } from '@angular/flex-layout';
import { MatProgressBarModule } from '@angular/material/progress-bar';
import { MatIconModule } from '@angular/material/icon';
import { MatDividerModule } from '@angular/material/divider';
import { MatButtonModule } from '@angular/material/button';
import { Color, NgxChartsModule, ScaleType } from '@swimlane/ngx-charts';
import { SwitchComponent } from '../components/switch/switch.component';

@Component({
  selector: 'app-stats',
  standalone: true,
  imports: [
    MatGridListModule,
    MatCardModule,
    FlexLayoutModule,
    MatProgressBarModule,
    MatButtonModule,
    MatDividerModule,
    MatIconModule,
    NgxChartsModule,
    SwitchComponent
  ],
  templateUrl: './stats.component.html',
  styleUrl: './stats.component.scss',
})
export class StatsComponent {
  isSmallScreen = false;

  title = ''

  mode: ApplicationMode = 'Books';

  constructor(
    breakpointObserver: BreakpointObserver,
    private store: MainStoreService,
  ) {
    breakpointObserver
      .observe([Breakpoints.XSmall, Breakpoints.Tablet])
      .subscribe((result) => {
        this.isSmallScreen = result.matches;
      });
  }

  ngOnInit() {
  this.store.setCurrentSubpage('Stats');

  this.store.mode$.subscribe((mode) => this.changeModeCallback(mode))
}

private changeModeCallback(mode: ApplicationMode) {
  this.mode = mode;

  this.title = this.mode === 'Books'
    ? 'Reading statistics'
    : 'Watching statistics'
}

  // MOCD DATA FOR THE CHART
  bookData: any[] = [
    {
      name: '2018',
      value: 10,
    },
    {
      name: '2019',
      value: 15,
    },
    {
      name: '2020',
      value: 20,
    },
  ];
  bookDataYear: any[] = [
    {
      name: '1',
      value: 10,
    },
    {
      name: '2',
      value: 15,
    },
    {
      name: '3',
      value: 20,
    },
    {
      name: '4',
      value: 10,
    },
    {
      name: '5',
      value: 15,
    },
    {
      name: '6',
      value: 20,
    },
    {
      name: '7',
      value: 10,
    },
    {
      name: '8',
      value: 15,
    },
    {
      name: '9',
      value: 20,
    },
    {
      name: '10',
      value: 10,
    },
    {
      name: '11',
      value: 15,
    },
    {
      name: '12',
      value: 20,
    },
  ];

  colorScheme: Color = {
    name: 'vivid',
    selectable: true,
    group: ScaleType.Ordinal,
    domain: ['#5AA454', '#A10A28', '#C7B42C', '#AAAAAA'],
  };
}
