import { Component, Inject } from "@angular/core";
import { MAT_DIALOG_DATA, MatDialogRef } from "@angular/material/dialog";
import { Router } from "@angular/router";
import { ButtonComponent } from "src/app/shared/components/button/button.component";

export interface DialogData {
  item: any;
}

@Component({
  selector: "app-details-dialog",
  standalone: true,
  imports: [ButtonComponent],
  templateUrl: "./details-dialog.component.html",
  styleUrl: "./details-dialog.component.scss",
})
export class DetailsDialogComponent {
  get item() {
    return this.data.item;
  }

  constructor(
    public dialogRef: MatDialogRef<DetailsDialogComponent>,
    @Inject(MAT_DIALOG_DATA) public data: DialogData,
    private router: Router
  ) {}

  onContinueClick() {
    this.close();
    this.router.navigate(["/current/"], {
      queryParams: { id: this.data.item.id },
    });

    // this.router.navigate(["/item/session"], {
    //   queryParams: { id: this.data.item.id },
    // });
  }

  close(): void {
    this.dialogRef.close();
  }

  onDeleteClick() {}
}
