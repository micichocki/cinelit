import { Injectable } from '@angular/core';
import { BehaviorSubject, Subject } from 'rxjs';

export type SubpageType = 'Home' | 'Current' | 'Collection' | 'Stats' | 'Settings'

export type ApplicationMode = 'Books' | 'Movies'

@Injectable({
  providedIn: 'root'
})
export class MainStoreService {
  private currentSubpage = new Subject<SubpageType>();
  
  currentSubpage$ = this.currentSubpage.asObservable();
  
  private modeSubject = new BehaviorSubject<ApplicationMode>('Books');
  
  mode$ = this.modeSubject.asObservable();

  mode: ApplicationMode = 'Books'

  constructor() { }

  setMode(mode: ApplicationMode) {
    this.modeSubject.next(mode);
    this.mode = mode;
  }

  setCurrentSubpage(subpage: SubpageType) {
    this.currentSubpage.next(subpage);
  }

}
