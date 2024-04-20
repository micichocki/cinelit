import { Component, Inject } from '@angular/core';
import { MAT_DIALOG_DATA, MatDialogRef } from '@angular/material/dialog';
import { ButtonComponent } from 'src/app/shared/components/button/button.component';

export interface DialogData {
  item: any;
}

@Component({
  selector: 'app-details-dialog',
  standalone: true,
  imports: [ButtonComponent],
  templateUrl: './details-dialog.component.html',
  styleUrl: './details-dialog.component.scss'
})
export class DetailsDialogComponent {
  get item() {
    return this.data.item;
  }

  constructor(
    public dialogRef: MatDialogRef<DetailsDialogComponent>,
    @Inject(MAT_DIALOG_DATA) public data: DialogData,
  ) {}

  onContinueClick() {

  }

  onCloseClick(): void {
    this.dialogRef.close();
  }

  onDeleteClick() {

  }
}
