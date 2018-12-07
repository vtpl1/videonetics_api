/**
 * Videonetics Visual Computing Platform
 * API to access the Videonetics Visual Computing Platform for analytics events
 *
 * OpenAPI spec version: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */
/* tslint:disable:no-unused-variable member-ordering */

import { Inject, Injectable, Optional }                      from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams,
         HttpResponse, HttpEvent }                           from '@angular/common/http';
import { CustomHttpUrlEncodingCodec }                        from '../encoder';

import { Observable }                                        from 'rxjs/Observable';

import { CameraId } from '../model/cameraId';
import { Cameras } from '../model/cameras';
import { EnterpriseId } from '../model/enterpriseId';

import { BASE_PATH, COLLECTION_FORMATS }                     from '../variables';
import { Configuration }                                     from '../configuration';


@Injectable()
export class VideosService {

    protected basePath = 'http://v2.videonetics.com:5000/';
    public defaultHeaders = new HttpHeaders();
    public configuration = new Configuration();

    constructor(protected httpClient: HttpClient, @Optional()@Inject(BASE_PATH) basePath: string, @Optional() configuration: Configuration) {
        if (basePath) {
            this.basePath = basePath;
        }
        if (configuration) {
            this.configuration = configuration;
            this.basePath = basePath || configuration.basePath || this.basePath;
        }
    }

    /**
     * @param consumes string[] mime-types
     * @return true: consumes contains 'multipart/form-data', false: otherwise
     */
    private canConsumeForm(consumes: string[]): boolean {
        const form = 'multipart/form-data';
        for (const consume of consumes) {
            if (form === consume) {
                return true;
            }
        }
        return false;
    }


    /**
     * Get all cameras for a enterprise
     * List all cameras for a enterprise.
     * @param enterpriseId enterprise Id
     * @param cameraId Camera Id
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public enterpriseIdCameraIdVideosGet(enterpriseId: EnterpriseId, cameraId: CameraId, observe?: 'body', reportProgress?: boolean): Observable<Cameras>;
    public enterpriseIdCameraIdVideosGet(enterpriseId: EnterpriseId, cameraId: CameraId, observe?: 'response', reportProgress?: boolean): Observable<HttpResponse<Cameras>>;
    public enterpriseIdCameraIdVideosGet(enterpriseId: EnterpriseId, cameraId: CameraId, observe?: 'events', reportProgress?: boolean): Observable<HttpEvent<Cameras>>;
    public enterpriseIdCameraIdVideosGet(enterpriseId: EnterpriseId, cameraId: CameraId, observe: any = 'body', reportProgress: boolean = false ): Observable<any> {
        if (enterpriseId === null || enterpriseId === undefined) {
            throw new Error('Required parameter enterpriseId was null or undefined when calling enterpriseIdCameraIdVideosGet.');
        }
        if (cameraId === null || cameraId === undefined) {
            throw new Error('Required parameter cameraId was null or undefined when calling enterpriseIdCameraIdVideosGet.');
        }

        let headers = this.defaultHeaders;

        // authentication (accessCode) required
        if (this.configuration.accessToken) {
            const accessToken = typeof this.configuration.accessToken === 'function'
                ? this.configuration.accessToken()
                : this.configuration.accessToken;
            headers = headers.set('Authorization', 'Bearer ' + accessToken);
        }

        // to determine the Accept header
        let httpHeaderAccepts: string[] = [
            'application/json'
        ];
        const httpHeaderAcceptSelected: string | undefined = this.configuration.selectHeaderAccept(httpHeaderAccepts);
        if (httpHeaderAcceptSelected != undefined) {
            headers = headers.set('Accept', httpHeaderAcceptSelected);
        }

        // to determine the Content-Type header
        const consumes: string[] = [
        ];

        return this.httpClient.get(`${this.basePath}/${encodeURIComponent(String(enterpriseId))}/${encodeURIComponent(String(cameraId))}/videos`,
            {
                withCredentials: this.configuration.withCredentials,
                headers: headers,
                observe: observe,
                reportProgress: reportProgress
            }
        );
    }

