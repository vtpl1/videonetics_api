package io.swagger.model;

import java.util.Objects;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonCreator;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import io.swagger.model.AccessStatus;
import io.swagger.model.Enterprise;
import io.swagger.model.EnterpriseAccountStatus;
import java.util.UUID;
import org.springframework.validation.annotation.Validated;
import javax.validation.Valid;
import javax.validation.constraints.*;

/**
 * EnterpriseDetail
 */
@Validated
@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.SpringCodegen", date = "2018-12-05T09:37:54.774Z[GMT]")

public class EnterpriseDetail extends AccessStatus  {
  @JsonProperty("id")
  private UUID id = null;

  @JsonProperty("name")
  private String name = null;

  @JsonProperty("logo")
  private String logo = null;

  @JsonProperty("address")
  private String address = null;

  @JsonProperty("contact")
  private String contact = null;

  @JsonProperty("accountStatus")
  private EnterpriseAccountStatus accountStatus = null;

  public EnterpriseDetail id(UUID id) {
    this.id = id;
    return this;
  }

  /**
   * Get id
   * @return id
  **/
  @ApiModelProperty(required = true, value = "")
  @NotNull

  @Valid

  public UUID getId() {
    return id;
  }

  public void setId(UUID id) {
    this.id = id;
  }

  public EnterpriseDetail name(String name) {
    this.name = name;
    return this;
  }

  /**
   * Get name
   * @return name
  **/
  @ApiModelProperty(required = true, value = "")
  @NotNull


  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }

  public EnterpriseDetail logo(String logo) {
    this.logo = logo;
    return this;
  }

  /**
   * Get logo
   * @return logo
  **/
  @ApiModelProperty(value = "")


  public String getLogo() {
    return logo;
  }

  public void setLogo(String logo) {
    this.logo = logo;
  }

  public EnterpriseDetail address(String address) {
    this.address = address;
    return this;
  }

  /**
   * Get address
   * @return address
  **/
  @ApiModelProperty(value = "")


  public String getAddress() {
    return address;
  }

  public void setAddress(String address) {
    this.address = address;
  }

  public EnterpriseDetail contact(String contact) {
    this.contact = contact;
    return this;
  }

  /**
   * Get contact
   * @return contact
  **/
  @ApiModelProperty(value = "")


  public String getContact() {
    return contact;
  }

  public void setContact(String contact) {
    this.contact = contact;
  }

  public EnterpriseDetail accountStatus(EnterpriseAccountStatus accountStatus) {
    this.accountStatus = accountStatus;
    return this;
  }

  /**
   * Get accountStatus
   * @return accountStatus
  **/
  @ApiModelProperty(required = true, value = "")
  @NotNull

  @Valid

  public EnterpriseAccountStatus getAccountStatus() {
    return accountStatus;
  }

  public void setAccountStatus(EnterpriseAccountStatus accountStatus) {
    this.accountStatus = accountStatus;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    EnterpriseDetail enterpriseDetail = (EnterpriseDetail) o;
    return Objects.equals(this.id, enterpriseDetail.id) &&
        Objects.equals(this.name, enterpriseDetail.name) &&
        Objects.equals(this.logo, enterpriseDetail.logo) &&
        Objects.equals(this.address, enterpriseDetail.address) &&
        Objects.equals(this.contact, enterpriseDetail.contact) &&
        Objects.equals(this.accountStatus, enterpriseDetail.accountStatus) &&
        super.equals(o);
  }

  @Override
  public int hashCode() {
    return Objects.hash(id, name, logo, address, contact, accountStatus, super.hashCode());
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class EnterpriseDetail {\n");
    sb.append("    ").append(toIndentedString(super.toString())).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    logo: ").append(toIndentedString(logo)).append("\n");
    sb.append("    address: ").append(toIndentedString(address)).append("\n");
    sb.append("    contact: ").append(toIndentedString(contact)).append("\n");
    sb.append("    accountStatus: ").append(toIndentedString(accountStatus)).append("\n");
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

