import { FormGroup } from "@angular/forms";
import { AbstractControl, ValidationErrors, ValidatorFn } from "@angular/forms";

export function markFormGroupTouched(formGroup: FormGroup) {
  Object.values(formGroup.controls).forEach((control) => {
    if (control instanceof FormGroup) {
      markFormGroupTouched(control);
    } else {
      control.markAsTouched();
    }
  });
}

export const passwordMatchesValidator: ValidatorFn = (
  control: AbstractControl
): ValidationErrors | null => {
  const password = control.get("password")?.value;
  const confirmPassword = control.get("confirmPassword")?.value;

  return password && confirmPassword && password === confirmPassword
    ? null
    : { passwordMismatch: true };
};

export const nameValidator: ValidatorFn = (
  control: AbstractControl
): ValidationErrors | null => {
  const nameRegex = /^[a-zA-Z\s]*$/;
  if (!nameRegex.test(control.value)) {
    return { specialCharacters: true };
  }
  return null;
};

export const passwordValidator: ValidatorFn = (
  control: AbstractControl
): ValidationErrors | null => {
  const passwordRegex = /^(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]*$/;
  if (!passwordRegex.test(control.value)) {
    return { invalidPassword: true };
  }
  return null;
};
