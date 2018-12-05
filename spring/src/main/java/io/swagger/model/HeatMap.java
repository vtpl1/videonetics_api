package io.swagger.model;

import java.util.Objects;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonCreator;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import io.swagger.model.VertexWithValue;
import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.List;
import org.springframework.validation.annotation.Validated;
import javax.validation.Valid;
import javax.validation.constraints.*;

/**
 * HeatMap
 */
@Validated
@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.SpringCodegen", date = "2018-12-05T07:09:15.776Z[GMT]")

public class HeatMap   {
  @JsonProperty("max")
  private BigDecimal max = null;

  @JsonProperty("verticesWithValue")
  @Valid
  private List<VertexWithValue> verticesWithValue = null;

  public HeatMap max(BigDecimal max) {
    this.max = max;
    return this;
  }

  /**
   * Get max
   * @return max
  **/
  @ApiModelProperty(example = "5", value = "")

  @Valid

  public BigDecimal getMax() {
    return max;
  }

  public void setMax(BigDecimal max) {
    this.max = max;
  }

  public HeatMap verticesWithValue(List<VertexWithValue> verticesWithValue) {
    this.verticesWithValue = verticesWithValue;
    return this;
  }

  public HeatMap addVerticesWithValueItem(VertexWithValue verticesWithValueItem) {
    if (this.verticesWithValue == null) {
      this.verticesWithValue = new ArrayList<VertexWithValue>();
    }
    this.verticesWithValue.add(verticesWithValueItem);
    return this;
  }

  /**
   * Get verticesWithValue
   * @return verticesWithValue
  **/
  @ApiModelProperty(value = "")

  @Valid

  public List<VertexWithValue> getVerticesWithValue() {
    return verticesWithValue;
  }

  public void setVerticesWithValue(List<VertexWithValue> verticesWithValue) {
    this.verticesWithValue = verticesWithValue;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    HeatMap heatMap = (HeatMap) o;
    return Objects.equals(this.max, heatMap.max) &&
        Objects.equals(this.verticesWithValue, heatMap.verticesWithValue);
  }

  @Override
  public int hashCode() {
    return Objects.hash(max, verticesWithValue);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class HeatMap {\n");
    
    sb.append("    max: ").append(toIndentedString(max)).append("\n");
    sb.append("    verticesWithValue: ").append(toIndentedString(verticesWithValue)).append("\n");
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

