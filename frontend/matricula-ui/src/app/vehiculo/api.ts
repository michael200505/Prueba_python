import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

export interface VehiculoIn {
  placa: string;
  propietario: string;
  marca: string;
  fabricacion: number;
  valor_comercial: number;
}

export interface VehiculoOut extends VehiculoIn {
  impuesto: number;
  codigo_revision: string;
}

@Injectable({ providedIn: 'root' })
export class ApiService {
  private baseUrl = 'http://127.0.0.1:8000/vehiculos';

  constructor(private http: HttpClient) {}

  crear(v: VehiculoIn): Observable<VehiculoOut> {
    return this.http.post<VehiculoOut>(this.baseUrl, v);
  }

  listar(): Observable<VehiculoOut[]> {
    return this.http.get<VehiculoOut[]>(this.baseUrl);
  }
}
