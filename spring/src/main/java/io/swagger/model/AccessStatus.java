package io.swagger.model;

import java.util.Objects;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonCreator;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import org.springframework.validation.annotation.Validated;
import javax.validation.Valid;
import javax.validation.constraints.*;

/**
 * AccessStatus
 */
@Validated
@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.SpringCodegen", date = "2018-11-21T13:08:36.940Z[GMT]")

public class AccessStatus   {
  @JsonProperty("createdOn")
  private Long createdOn = null;

  @JsonProperty("lastAccesseOn")
  private Long lastAccesseOn = null;

  @JsonProperty("firstAccesseOn")
  private Long firstAccesseOn = null;

  @JsonProperty("onlineTimeInSec")
  private Float onlineTimeInSec = null;

  public AccessStatus createdOn(Long createdOn) {
    this.createdOn = createdOn;
    return this;
  }

  /**
   * Get createdOn
   * @return createdOn
  **/
  @ApiModelProperty(value = "")


  public Long getCreatedOn() {
    return createdOn;
  }

  public void setCreatedOn(Long createdOn) {
    this.createdOn = createdOn;
  }

  public AccessStatus lastAccesseOn(Long lastAccesseOn) {
    this.lastAccesseOn = lastAccesseOn;
    return this;
  }

  /**
   * Get lastAccesseOn
   * @return lastAccesseOn
  **/
  @ApiModelProperty(value = "")


  public Long getLastAccesseOn() {
    return lastAccesseOn;
  }

  public void setLastAccesseOn(Long lastAccesseOn) {
    this.lastAccesseOn = lastAccesseOn;
  }

  public AccessStatus firstAccesseOn(Long firstAccesseOn) {
    this.firstAccesseOn = firstAccesseOn;
    return this;
  }

  /**
   * Get firstAccesseOn
   * @return firstAccesseOn
  **/
  @ApiModelProperty(value = "")


  public Long getFirstAccesseOn() {
    return firstAccesseOn;
  }

  public void setFirstAccesseOn(Long firstAccesseOn) {
    this.firstAccesseOn = firstAccesseOn;
  }

  public AccessStatus onlineTimeInSec(Float onlineTimeInSec) {
    this.onlineTimeInSec = onlineTimeInSec;
    return this;
  }

  /**
   * Get onlineTimeInSec
   * @return onlineTimeInSec
  **/
  @ApiModelProperty(value = "")


  public Float getOnlineTimeInSec() {
    return onlineTimeInSec;
  }

  public void setOnlineTimeInSec(Float onlineTimeInSec) {
    this.onlineTimeInSec = onlineTimeInSec;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AccessStatus accessStatus = (AccessStatus) o;
    return Objects.equals(this.createdOn, accessStatus.createdOn) &&
        Objects.equals(this.lastAccesseOn, accessStatus.lastAccesseOn) &&
        Objects.equals(this.firstAccesseOn, accessStatus.firstAccesseOn) &&
        Objects.equals(this.onlineTimeInSec, accessStatus.onlineTimeInSec);
  }

  @Override
  public int hashCode() {
    return Objects.hash(createdOn, lastAccesseOn, firstAccesseOn, onlineTimeInSec);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AccessStatus {\n");
    
    sb.append("    createdOn: ").append(toIndentedString(createdOn)).append("\n");
    sb.append("    lastAccesseOn: ").append(toIndentedString(lastAccesseOn)).append("\n");
    sb.append("    firstAccesseOn: ").append(toIndentedString(firstAccesseOn)).append("\n");
    sb.append("    onlineTimeInSec: ").append(toIndentedString(onlineTimeInSec)).append("\n");
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

