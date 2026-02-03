import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormBuilder, ReactiveFormsModule, Validators } from '@angular/forms';
import { ApiService, VehiculoOut } from './api';

@Component({
  selector: 'app-vehiculo',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule],
  templateUrl: './vehiculo.html',
  styleUrl: './vehiculo.css',
})
export class VehiculoComponent {
  vehiculos: VehiculoOut[] = [];
  error = '';
  form;

  constructor(private fb: FormBuilder, private api: ApiService) {
    this.form = this.fb.group({
      placa: ['', Validators.required],
      propietario: ['', Validators.required],
      marca: ['', Validators.required],
      fabricacion: [2020, Validators.required],
      valor_comercial: [0, [Validators.required, Validators.min(0)]],
    });

    this.listar();
  }

  listar() {
    this.api.listar().subscribe(v => (this.vehiculos = v));
  }

  guardar() {
    if (this.form.invalid) return;

    this.api.crear(this.form.value as any).subscribe({
      next: () => {
        this.form.reset({ fabricacion: 2020, valor_comercial: 0 });
        this.listar();
      },
      error: (e) => this.error = e?.error?.detail ?? 'Error'
    });
  }

  peligro(v: VehiculoOut) {
    return v.impuesto > 500;
  }
}
