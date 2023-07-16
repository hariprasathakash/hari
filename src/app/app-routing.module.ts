import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { SingupComponent } from './signup/signup.component';
import { DashboardComponent } from './dashboard/dashboard.component';
// import { ResultComponent } from './result/result.component';
// import {PredictComponent} from './predict/predict.component';

const routes: Routes = [
  {path:'', component: LoginComponent},
  {path:'login', component:LoginComponent},
  {path:'singup', component:SingupComponent},
  {path:'dashboard', component:DashboardComponent},
  // {path:'result', component:ResultComponent}
  // {path:'predict', component:PredictComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
