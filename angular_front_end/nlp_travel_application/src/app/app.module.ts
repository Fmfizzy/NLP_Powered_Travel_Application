import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { ChartModule } from 'angular-highcharts';
import { AppComponent } from './app.component';
import { ChartComponent } from './chart/chart.component';
import { LinkifyPipe } from './linkify.pipe';

@NgModule({
  declarations: [
    AppComponent,
    ChartComponent,
    LinkifyPipe
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpClientModule,
    ChartModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }