import { Component, Input } from '@angular/core';
import { Chart } from 'angular-highcharts';
import * as Highcharts from 'highcharts';

@Component({
  selector: 'app-chart',
  template: `
    <div [chart]="chart" style="height: 200px; width: 400px; display: flex;"></div>
  `
})
export class ChartComponent {
  @Input() plotData: any[] = [];
  chart: Chart = new Chart;

  ngOnInit() {
    this.createDiseaseChart();
  }

  ngOnChanges() {
    this.createDiseaseChart();
  }

  formatData(data: any[]) {
    return data.map(item => {
      const date = new Date(item.date).getTime();
      return [date, item.total_diseases];
    });
  }

  createDiseaseChart() {
    this.chart = new Chart({
      chart: {
        type: 'line'
      },
      title: {
        text: 'Total Diseases'
      },
      credits: {
        enabled: false
      },
      xAxis: {
        type: 'datetime',
        title: {
          text: 'Time'
        }
      },
      yAxis: {
        title: {
          text: 'People infected'
        }
      },
      series: [
        {
          type: 'line',
          name: 'Total Diseases',
          data: this.formatData(this.plotData)
        }
      ]
    });
  }
}