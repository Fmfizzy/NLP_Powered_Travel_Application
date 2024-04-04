import { Component, ViewChild } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Chart } from 'angular-highcharts';
import * as Highcharts from 'highcharts';
import { LinkifyPipe } from './linkify.pipe'; 


interface ChatMessage {
  type: 'user' | 'bot';
  text: string;
  plotData?: any[];
}

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {

  searchTerm: string = '';
  messageInput: string = '';
  userPrompt: string = '';
  chatMessages: string[] = [];
  botMessages: string[] = [];
  messages: ChatMessage[] = [{ type: 'bot', text: "Hello there!😊 Where would you like to go and what type of activity are you in the mood for?" }];
  showChart: boolean = false;
  highcharts = Highcharts;
  lineChart: Chart = new Chart;
  tempPrompt: string = "";



  constructor(private http: HttpClient) { }

  sendMessage() {
    const url = 'http://127.0.0.1:5000/search';
    this.userPrompt = this.messageInput;
    this.messageInput = '';
    this.messages.push({ type: 'user', text: this.userPrompt });
  
    if (!this.userPrompt.trim()) {
      this.messages.push({ type: 'bot', text: 'Please provide a valid input.' });
      return;
    }
  
    this.http.post(url, { term: this.userPrompt }).subscribe(
      (response: any) => {
        const { location, activity_preference, district, top_activity_types, top_activities, plot_data } = response;
  
        if (!location || !activity_preference) {
          this.messages.push({ type: 'bot', text: 'Please provide a valid user prompt!.' }); 
          this.messages.push({ type: 'bot', text: "Eg: I wish to go to 'City Name' and would prefer 'Activity Preference'" }); 
        } else {
          let index = 0;
          // Handle top activities
          top_activities.forEach((activityGroup: any[]) => {
            const [activityTypeLabel, activityTypeScore] = top_activity_types[index];
            const formattedActivityType = activityTypeLabel
              .replace(/_/g, ' ')
              .split(' ')
              .map((word: string) => word.charAt(0).toUpperCase() + word.slice(1))
              .join(' ');
          
            this.messages.push({ type: 'bot', text: `Activity Type: ${formattedActivityType}` });
            activityGroup.forEach((place: any[]) => {
              const [name, , , , maps_link] = place;
              const messageText = `${name}: ${maps_link}`;
              this.messages.push({ type: 'bot', text: messageText });
            });
            index++; 
          });

          // Handle plot data
          if (plot_data) {
            const plotDataResponse = `Infectious disease spread in ${district} for the year 2023`;
            this.messages.push({ type: 'bot', text: plotDataResponse, plotData: plot_data });
            this.showChart = true;
          }
        }
      },
      (error) => {
        console.error('Error sending search term:', error);
      }
    );
  }
}

  // formatData(data: any[]) {
  //   return data.map(item => {
  //     const date = new Date(item.date).getTime();
  //     return [date, item.total_diseases];
  //   });
  // }

  // createDiseaseChart(plotData: any[]) {
  //   this.lineChart = new Chart({
  //     chart: {
  //       type: 'line'
  //     },
  //     title: {
  //       text: 'Total Diseases'
  //     },
  //     credits: {
  //       enabled: false
  //     },
  //     xAxis: {
  //       type: 'datetime',
  //       title: {
  //         text: 'Time'
  //       }
  //     },
  //     yAxis: {
  //       title: {
  //         text: 'Number of people infected'
  //       }
  //     },
  //     series: [
  //       {
  //         type: 'line',
  //         name: 'Total Diseases',
  //         data: this.formatData(plotData)
  //       }
  //     ]
  //   });}

  // sendMessage() {
  //   const url = 'http://127.0.0.1:5000/search';
  //   this.http.post(url, { term: this.messageInput }).subscribe(
  //     response => {
  //       console.log('Search term sent to backend:', response);
  //     },
  //     error => {
  //       console.error('Error sending search term:', error);
  //     }
  //   );

  //   // Get responses function
  //   if (this.messageInput.trim() !== '') {
  //     this.messages.push({ type: 'user', text: this.messageInput });
  //     const botResponse = 'This is a sample bot response to your message: ' + this.messageInput;
  //     this.messages.push({ type: 'bot', text: botResponse });
  //     this.messageInput = '';
  //   }
  // }

    // sendSearchTerm() {
  //   const url = 'http://127.0.0.1:5000/search';
  //   this.http.post(url, { term: this.searchTerm }).subscribe(
  //     response => {
  //       console.log('Search term sent to backend:', response);
  //     },
  //     error => {
  //       console.error('Error sending search term:', error);
  //     }
  //   );
  // }
