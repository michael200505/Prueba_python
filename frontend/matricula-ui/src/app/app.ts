import { Component } from '@angular/core';
import { VehiculoComponent } from './vehiculo/vehiculo';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [VehiculoComponent],
  templateUrl: './app.html',
  styleUrl: './app.css',
})
export class App {
peligro(_t32: any) {
throw new Error('Method not implemented.');
}
}
