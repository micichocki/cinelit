import { Component } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute, Router, RouterLink } from '@angular/router';
import { map } from 'rxjs';
import { ButtonComponent } from 'src/app/shared/components/button/button.component';
import { InputComponent } from 'src/app/shared/components/input/input.component';
import { markFormGroupTouched } from 'src/app/shared/helpers/validation';
import { APIMovie } from 'src/app/shared/models/movies';
import { RepositoryService } from 'src/app/shared/services/repository.service';

@Component({
  selector: 'app-add-item',
  standalone: true,
  imports: [InputComponent, ButtonComponent, RouterLink],
  templateUrl: './add-item.component.html',
  styleUrl: './add-item.component.scss'
})
export class AddItemComponent {
  bookForm = new FormGroup({
    title: new FormControl('', Validators.required),
    author: new FormControl('', Validators.required),
    pages: new FormControl(0, Validators.required),
    genre: new FormControl('', Validators.required),
    posterUrl: new FormControl('', Validators.required),
  });

  movieForm = new FormGroup({
    title: new FormControl('', Validators.required),
    genre: new FormControl('', Validators.required),
    director: new FormControl('', Validators.required),
    length: new FormControl('', Validators.required),
    posterUrl: new FormControl('', Validators.required),
  });

  // file!: File;

  src: string = '';

  type = 'book';

  constructor(
      private activatedRoute: ActivatedRoute,
      private repositoryService: RepositoryService,
      private router: Router
    ) {
    this.activatedRoute.queryParams.subscribe(params => {
          let type = params['type'];
          this.type = type;
      });
  }

  onSaveClick() {
    const formData = this.type === 'book' ? this.bookForm : this.movieForm
    markFormGroupTouched(formData);

    if (!formData.valid) return;

    // const formData: FormData = new FormData();

    // if (this.file) {
    //   formData.append('file', this.file, this.file.name);
    // }
    
    if (this.type === 'book') {
      this.addBook(formData);
    }
    else if(this.type === 'movie') {
      this.addMovie(formData);
    }
  }

  onSearchClick() {
    if (this.type === 'book' && this.bookForm.value.title) {
      this.repositoryService
        .searchBookByTitle(this.bookForm.value.title)
        .subscribe(b => { 
          if (b) {
            this.bookForm.patchValue(b) 
          }
        })
    }
    else if (this.movieForm.value.title){
      this.repositoryService
      .searchMovieByTitle(this.movieForm.value.title)
      .pipe(
        map((apiMovie: APIMovie) => {
          return {
            title: apiMovie.Title,
            genre: apiMovie.Genre,
            director: apiMovie.Director,
            length: apiMovie.Runtime,
            posterUrl: apiMovie.Poster
          }
        })
      )
      .subscribe((b) => { 
        if (b) {
          this.movieForm.patchValue(b) 
        }
      })
    }
  }

  private addMovie(formData: FormGroup) {
    const newMovie = {
      title: this.movieForm.value.title,
      genre: this.movieForm.value.genre,
      director: this.movieForm.value.director,
      length: this.movieForm.value.length,
    }

    // formData.append('newItem', JSON.stringify(newMovie));
    

    this.repositoryService.addMovie(formData).subscribe({
      next: () => this.router.navigate(['/collection']),
      error: (e: any) => {
        console.log(e)
      }
    });
  }

  private addBook(formData: FormGroup) {
    const newBook = {
      title: this.bookForm.value.title,
      author: this.bookForm.value.author,
      pages: this.bookForm.value.pages,
      genre: this.bookForm.value.genre,
    }

    // formData.append('newItem', JSON.stringify(newBook));

    this.repositoryService.addMovie(formData).subscribe({
      next: () => this.router.navigate(['/collection']),
      error: (e: any) => {
        console.log(e)
      }
    });
  }

  // onFileSelected(event: any) {
  //   this.file = event.target.files[0];

  //   this.src = URL.createObjectURL(this.file);
  // }
}
