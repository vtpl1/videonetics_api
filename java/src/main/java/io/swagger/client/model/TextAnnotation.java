/*
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

package io.swagger.client.model;

import java.util.Objects;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.client.model.BoundingBox;
import io.swagger.client.model.Locale;
import io.swagger.v3.oas.annotations.media.Schema;
import java.io.IOException;

/**
 * TextAnnotation
 */

@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.JavaClientCodegen", date = "2018-12-07T13:54:39.197Z[GMT]")public class TextAnnotation {

  @SerializedName("locale")
  private Locale locale = null;

  @SerializedName("description")
  private String description = null;

  @SerializedName("boundingPoly")
  private BoundingBox boundingPoly = null;
  public TextAnnotation locale(Locale locale) {
    this.locale = locale;
    return this;
  }

  

  /**
  * Get locale
  * @return locale
  **/
  @Schema(description = "")
  public Locale getLocale() {
    return locale;
  }
  public void setLocale(Locale locale) {
    this.locale = locale;
  }
  public TextAnnotation description(String description) {
    this.description = description;
    return this;
  }

  

  /**
  * Get description
  * @return description
  **/
  @Schema(example = "WB02AB1234", description = "")
  public String getDescription() {
    return description;
  }
  public void setDescription(String description) {
    this.description = description;
  }
  public TextAnnotation boundingPoly(BoundingBox boundingPoly) {
    this.boundingPoly = boundingPoly;
    return this;
  }

  

  /**
  * Get boundingPoly
  * @return boundingPoly
  **/
  @Schema(description = "")
  public BoundingBox getBoundingPoly() {
    return boundingPoly;
  }
  public void setBoundingPoly(BoundingBox boundingPoly) {
    this.boundingPoly = boundingPoly;
  }
  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TextAnnotation textAnnotation = (TextAnnotation) o;
    return Objects.equals(this.locale, textAnnotation.locale) &&
        Objects.equals(this.description, textAnnotation.description) &&
        Objects.equals(this.boundingPoly, textAnnotation.boundingPoly);
  }

  @Override
  public int hashCode() {
    return java.util.Objects.hash(locale, description, boundingPoly);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TextAnnotation {\n");
    
    sb.append("    locale: ").append(toIndentedString(locale)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    boundingPoly: ").append(toIndentedString(boundingPoly)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(java.lang.Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }

}
