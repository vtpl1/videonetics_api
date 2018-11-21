package io.swagger.model;

import java.util.Objects;
import com.fasterxml.jackson.annotation.JsonValue;
import org.springframework.validation.annotation.Validated;
import javax.validation.Valid;
import javax.validation.constraints.*;

import com.fasterxml.jackson.annotation.JsonCreator;

/**
 * Gets or Sets enterpriseAccountStatus
 */
public enum EnterpriseAccountStatus {
  
  ACTIVE("active"),
  
  INACTIVE("inactive");

  private String value;

  EnterpriseAccountStatus(String value) {
    this.value = value;
  }

  @Override
  @JsonValue
  public String toString() {
    return String.valueOf(value);
  }

  @JsonCreator
  public static EnterpriseAccountStatus fromValue(String text) {
    for (EnterpriseAccountStatus b : EnterpriseAccountStatus.values()) {
      if (String.valueOf(b.value).equals(text)) {
        return b;
      }
    }
    return null;
  }
}

