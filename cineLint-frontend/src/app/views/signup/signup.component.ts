import {
  Component,
  OnInit,
  ChangeDetectionStrategy,
  EventEmitter,
  Output,
} from "@angular/core";
import { CommonModule } from "@angular/common";
import { Router, RouterModule } from "@angular/router";
import {
  ReactiveFormsModule,
  Validators,
  FormBuilder,
  FormGroup,
} from "@angular/forms";
import {
  passwordMatchesValidator,
  nameValidator,
  passwordValidator,
} from "../../shared/helpers/validation";
import { MatFormFieldModule } from "@angular/material/form-field";
import { MatInputModule } from "@angular/material/input";
import { MatButtonModule } from "@angular/material/button";

@Component({
  selector: "app-signup-form",
  standalone: true,
  imports: [
    CommonModule,
    ReactiveFormsModule,
    MatFormFieldModule,
    MatInputModule,
    MatButtonModule,
    RouterModule,
  ],
  templateUrl: "./signup.component.html",
  styleUrl: "./signup.component.scss",
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class SignupFormComponent implements OnInit {
  @Output() createUser = new EventEmitter<any>();

  signup = false;
  passwordMismatch = false;

  signupForm!: FormGroup;

  constructor(private fb: FormBuilder, private router: Router) {}

  ngOnInit(): void {
    this.signupForm = this.fb.group(
      {
        name: ["", [Validators.required, nameValidator]],
        lastName: ["", [Validators.required, nameValidator]],
        email: ["", [Validators.email, Validators.required]],
        password: [
          "",
          [Validators.minLength(8), Validators.required, passwordValidator],
        ],
        confirmPassword: ["", [Validators.minLength(8), Validators.required]],
      },
      {
        validators: [passwordMatchesValidator],
      }
    );
  }

  onSubmit(): void {
    this.createUser.emit(this.signupForm.getRawValue());
    this.signupForm.reset();
    this.router.navigate(["/login"]);
  }
}
