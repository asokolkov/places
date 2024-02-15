export interface PlacelistUser {
	id: string;
	name: string;
}


export interface PlacelistCompressed {
	id: string;
	name: string;
	author: PlacelistUser;
}


export interface PlacelistsList {
	placelists: PlacelistCompressed[];
}


export interface PlacelistPlace {
	id: string;
	name: string;
	address: string;
}


export interface Placelist {
	id: string;
	name: string;
	author: PlacelistUser;
	places: PlacelistPlace[];
}


export interface PlacelistCreate {
	name: string;
}


export interface PlacelistUpdate {
	name: string;
	places_ids: string[];
}
