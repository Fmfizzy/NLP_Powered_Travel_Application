import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'linkify'
})
export class LinkifyPipe implements PipeTransform {
  transform(text: string): string {
    const pattern = /(https?:\/\/[^\s]+)/g;
    return text.replace(pattern, '<a href="$1" target="_blank">$1</a>');
  }
}