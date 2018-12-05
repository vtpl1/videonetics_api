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
import io.swagger.v3.oas.annotations.media.Schema;
import java.io.IOException;

/**
 * FaceAnnotation
 */

@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.JavaClientCodegen", date = "2018-12-05T12:34:15.370Z[GMT]")public class FaceAnnotation {

  @SerializedName("boundingBox")
  private BoundingBox boundingBox = null;

  @SerializedName("tightBoundingBox")
  private BoundingBox tightBoundingBox = null;
  public FaceAnnotation boundingBox(BoundingBox boundingBox) {
    this.boundingBox = boundingBox;
    return this;
  }

  

  /**
  * Get boundingBox
  * @return boundingBox
  **/
  @Schema(description = "")
  public BoundingBox getBoundingBox() {
    return boundingBox;
  }
  public void setBoundingBox(BoundingBox boundingBox) {
    this.boundingBox = boundingBox;
  }
  public FaceAnnotation tightBoundingBox(BoundingBox tightBoundingBox) {
    this.tightBoundingBox = tightBoundingBox;
    return this;
  }

  

  /**
  * Get tightBoundingBox
  * @return tightBoundingBox
  **/
  @Schema(description = "")
  public BoundingBox getTightBoundingBox() {
    return tightBoundingBox;
  }
  public void setTightBoundingBox(BoundingBox tightBoundingBox) {
    this.tightBoundingBox = tightBoundingBox;
  }
  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    FaceAnnotation faceAnnotation = (FaceAnnotation) o;
    return Objects.equals(this.boundingBox, faceAnnotation.boundingBox) &&
        Objects.equals(this.tightBoundingBox, faceAnnotation.tightBoundingBox);
  }

  @Override
  public int hashCode() {
    return java.util.Objects.hash(boundingBox, tightBoundingBox);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class FaceAnnotation {\n");
    
    sb.append("    boundingBox: ").append(toIndentedString(boundingBox)).append("\n");
    sb.append("    tightBoundingBox: ").append(toIndentedString(tightBoundingBox)).append("\n");
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
