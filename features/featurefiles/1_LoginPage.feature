# ----------------------------------------------------------------------------
# File: LoginPage.feature
# Autor: Kosalram
# Date: 8-9-2016
# ----------------------------------------------------------------------------

Feature: Login page verification and validation.

  @valid_login_page
  Scenario: Verify login page with valid credientials
    Given Open the url
    When  Valid username and password entered
    Then  Sucessfully logged in and displaying the dashboard page





