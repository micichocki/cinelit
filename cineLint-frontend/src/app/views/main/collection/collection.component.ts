import { Component } from '@angular/core';
import { ApplicationMode, MainStoreService } from '../store/main-store.service';
import { SwitchComponent } from '../components/switch/switch.component';
import { CollectionResponse, RepositoryService } from 'src/app/shared/services/repository.service';
import { MatDialog } from '@angular/material/dialog';
import { DetailsDialogComponent } from '../components/details-dialog/details-dialog.component';

@Component({
  selector: 'app-collection',
  standalone: true,
  imports: [SwitchComponent],
  templateUrl: './collection.component.html',
  styleUrl: './collection.component.scss'
})
export class CollectionComponent {
  mode: ApplicationMode = 'Books';

  title = "asa";

  repositoryObjects: CollectionResponse | null = null;

  userId = 1;

  get selectedRespositoryObjects() { 
    return this.mode === 'Books'
      ? this.repositoryObjects?.books
      : this.repositoryObjects?.movies
  }

  constructor(
      private store: MainStoreService,
      private repositoryService: RepositoryService,
      public dialog: MatDialog
  ) {}
  ngOnInit() {
    this.store.setCurrentSubpage('Collection');

    this.store.mode$.subscribe((mode) => this.changeModeCallback(mode))

    this.repositoryService.getCollectionByUserId(this.userId).subscribe((res) => this.repositoryObjects = res)
  }

  private changeModeCallback(mode: ApplicationMode) {
    this.mode = mode;

    this.title = this.mode === 'Books'
      ? 'Your books collection'
      : 'Your film collection'
  }

  openDialog(item: any): void {
    const dialogRef = this.dialog.open(DetailsDialogComponent, {
      data: { item },
      panelClass: 'dialog'
    });

    dialogRef.afterClosed().subscribe(result => {
      console.log('The dialog was closed');
    });
  }
}
