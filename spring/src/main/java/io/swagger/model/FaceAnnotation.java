package io.swagger.model;

import java.util.Objects;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonCreator;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import io.swagger.model.BoundingBox;
import org.springframework.validation.annotation.Validated;
import javax.validation.Valid;
import javax.validation.constraints.*;

/**
 * FaceAnnotation
 */
@Validated
@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.SpringCodegen", date = "2018-12-05T09:37:54.774Z[GMT]")

public class FaceAnnotation   {
  @JsonProperty("boundingBox")
  private BoundingBox boundingBox = null;

  @JsonProperty("tightBoundingBox")
  private BoundingBox tightBoundingBox = null;

  public FaceAnnotation boundingBox(BoundingBox boundingBox) {
    this.boundingBox = boundingBox;
    return this;
  }

  /**
   * Get boundingBox
   * @return boundingBox
  **/
  @ApiModelProperty(value = "")

  @Valid

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
  @ApiModelProperty(value = "")

  @Valid

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
    return Objects.hash(boundingBox, tightBoundingBox);
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

