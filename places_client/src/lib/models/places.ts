export interface Place {
    id: string;
    name: string;
    address: string;
    latitude: number;
    longitude: number;
}

export interface PlacesList {
    places: Place[];
}

export interface PlaceCreate {
    name: string;
    address: string;
    latitude: number;
    longitude: number;
}
