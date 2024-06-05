import { Component, Inject } from "@angular/core";
import { MAT_DIALOG_DATA, MatDialogRef } from "@angular/material/dialog";
import { Router } from "@angular/router";
import { ButtonComponent } from "src/app/shared/components/button/button.component";
import { Book, Movie } from "src/app/shared/services/repository.service";

export interface DialogData {
  item: Book | Movie;
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

  isBook(item: any): item is Book {
    return (this.data.item as any).num_of_pages;
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
