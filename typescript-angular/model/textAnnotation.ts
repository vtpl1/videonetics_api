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
 */import { BoundingBox } from './boundingBox';
import { Locale } from './locale';


export interface TextAnnotation { 
    locale?: Locale;
    description?: string;
    boundingPoly?: BoundingBox;
}