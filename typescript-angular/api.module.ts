import { NgModule, ModuleWithProviders, SkipSelf, Optional } from '@angular/core';
import { Configuration } from './configuration';
import { HttpClient } from '@angular/common/http';


import { CamerasService } from './api/cameras.service';
import { EnterprisesService } from './api/enterprises.service';
import { EventsService } from './api/events.service';
import { TagsService } from './api/tags.service';
import { VideosService } from './api/videos.service';

@NgModule({
  imports:      [],
  declarations: [],
  exports:      [],
  providers: [
    CamerasService,
    EnterprisesService,
    EventsService,
    TagsService,
    VideosService ]
})
export class ApiModule {
    public static forRoot(configurationFactory: () => Configuration): ModuleWithProviders {
        return {
            ngModule: ApiModule,
            providers: [ { provide: Configuration, useFactory: configurationFactory } ]
        };
    }

    constructor( @Optional() @SkipSelf() parentModule: ApiModule,
                 @Optional() http: HttpClient) {
        if (parentModule) {
            throw new Error('ApiModule is already loaded. Import in your base AppModule only.');
        }
        if (!http) {
            throw new Error('You need to import the HttpClientModule in your AppModule! \n' +
            'See also https://github.com/angular/angular/issues/20575');
        }
    }
}
