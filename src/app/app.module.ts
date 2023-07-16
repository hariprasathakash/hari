import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

import { DashboardComponent } from './dashboard/dashboard.component';
import { LoginComponent } from './login/login.component';
import { SingupComponent } from './signup/signup.component';
import {FormsModule,ReactiveFormsModule} from '@angular/forms'
import { HttpClientModule } from '@angular/common/http';
import { CommonModule } from '@angular/common';
// import { PredictComponent } from './predict/predict.component';
// import { PredictComponent } from './predict/predict.component';
// import { ResultComponent } from './result/result.component';


@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    SingupComponent,
    DashboardComponent,
    // PredictComponent
    // PredictComponent,
    // ResultComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    ReactiveFormsModule,
    FormsModule,
    HttpClientModule,
    CommonModule
  ],
  providers:[],
  bootstrap: [AppComponent]
})
export class AppModule{}


