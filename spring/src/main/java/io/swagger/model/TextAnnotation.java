package io.swagger.model;

import java.util.Objects;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonCreator;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import io.swagger.model.BoundingBox;
import io.swagger.model.Locale;
import org.springframework.validation.annotation.Validated;
import javax.validation.Valid;
import javax.validation.constraints.*;

/**
 * TextAnnotation
 */
@Validated
@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.SpringCodegen", date = "2018-11-21T13:08:36.940Z[GMT]")

public class TextAnnotation   {
  @JsonProperty("locale")
  private Locale locale = null;

  @JsonProperty("description")
  private String description = null;

  @JsonProperty("boundingPoly")
  private BoundingBox boundingPoly = null;

  public TextAnnotation locale(Locale locale) {
    this.locale = locale;
    return this;
  }

  /**
   * Get locale
   * @return locale
  **/
  @ApiModelProperty(value = "")

  @Valid

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
  @ApiModelProperty(example = "WB02AB1234", value = "")


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
  @ApiModelProperty(value = "")

  @Valid

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
    return Objects.hash(locale, description, boundingPoly);
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

