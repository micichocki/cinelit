import { HttpInterceptorFn } from '@angular/common/http';
import { AuthService } from './shared/services/auth.service';
import { inject } from '@angular/core';

export const tokenInterceptor: HttpInterceptorFn = (req, next) => {
  const auth = inject(AuthService);

  // Clone the request and add the authorization header
  const authReq = req.clone({
    setHeaders: {
      Authorization: `Token ${auth.token}`
    }
  });

  return next(authReq);
};