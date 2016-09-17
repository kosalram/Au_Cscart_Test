# ----------------------------------------------------------------------------
# File: AddProduct.feature
# Autor: Kosalram
# Date: 14-9-2016
# ----------------------------------------------------------------------------



Feature: Product Functionality

  @add_valid_product
  Scenario: Add valid product into the system
    Given Login with valid credientials
    When Adding valid product
    Then Sucessfully added into the system