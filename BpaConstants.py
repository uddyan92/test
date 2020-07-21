"""
This file supports xpath for BPA 2.1.1 version
"""
BPA__VERSION = '2.2.1'
BPA__SLEEP_TO_VIEW = 2
BPA__MIN_SLEEP = 6
BPA__MID_SLEEP = 10
BPA__MAX_SLEEP = 25
# wait time in seconds
BPA__ADD_FORM_WAIT_TIME = 20
BPA__EDIT_FORM_WAIT_TIME = 10
BPA__DEVICE_SUCCESS_TIME = 10
BPA__DEVICE_DRIVER_WAIT_TIME = 20
BPA__WAIT_TIME = 60
BPA__MAX_WAIT_TIME = 30
BPA__MAX_TEMPLATE_WAIT_TIME = 80
BPA__TOAST_MSG_DISAPPEAR_TIME = 20
#OS upgrade XPATHS
BPA_OS_UPGRADE_TILE_XPATH = '//h5[@class="parent-highlight top-20 new-label" and contains(text(),"STC OS Upgrade")]//ancestor::div[@class="mdl-cell mdl-cell--3-col show ng-star-inserted"]'
BPA__SELECT_LATER_DATE= '/html/body/app-root/div/lib-osupgrade-order/div/div/div/div/form/div[1]/div/div[5]/div/mat-radio-group/mat-radio-button[2]/label/div[1]/div[1]'
BPA__SELECT_CALENDAR_BUTTON = '/html/body/app-root/div/lib-osupgrade-order/div/div/div/div/form/div[1]/div/div[5]/div[2]/div/mat-form-field/div/div[1]/div[2]/mat-datepicker-toggle/button'
BPA__SELECT_CALENDAR_DATE = '//div[@class = "mat-calendar-body-cell-content mat-calendar-body-selected mat-calendar-body-today"]'
BPA__XPATH_BATCH_SIZE_ERROR = '//p[@class="extra-error ng-star-inserted"]'
BPA__SELECT_TIME_VALUE = '//p[@class = "extra-error ng-star-inserted"]'
BPA__SELECT_PARALLEL = '/html/body/app-root/div/lib-osupgrade-order/div/div/div/div/form/div[1]/div/div[4]/div/mat-radio-group/mat-radio-button[2]/label/div[1]/div[1]'
BPA__SELECT_PARALLEL_ARROW = '/html/body/app-root/div/lib-osupgrade-order/div/div/div/div/form/div[1]/div/div[4]/div[2]/mat-form-field/div/div[1]/div/mat-select/div/div[2]'
BPA__SELECT_PARALLEL_BATCH = '/html/body/div/div[2]/div/div/div/mat-option[3]/span'
BPA__SELECT_PARALLEL_BATCH_10 = '/html/body/div/div[2]/div/div/div/mat-option[10]/span'
BPA__SELECT_PARALLEL_BATCH_2 = '/html/body/div/div[2]/div/div/div/mat-option[2]/span'
BPA_SELECT_DEVICE_LBL_TILE = '//h5[contains(text(),"Select Device")]'
BPA__CLICK_DEVICE_XPATH = '//mat-select[@placeholder="Select Device type" and @role="listbox"]'
BPA__SELECT_DEVICE_XPATH = '//span[@class="mat-option-text"]//child::span[text()= "{}"]'
BPA__SELECT_DEVICE_XPATH1 = '//span[contains(text(),"{}")]'
BPA__SELECT_ALL_MULTI= '//div[@class= "pure-checkbox select-all ng-star-inserted"]'
BPA__SELECT_LATER = '//div[contains(text(), "Later")]'
BPA__CALENDAR_CLCK = '//svg[@class = "mat-datepicker-toggle-default-icon ng-star-inserted"]'
BPA__DATE_CLICK = '//div[@class="mat-calendar-body-cell-content mat-calendar-body-today" and contains(text(),8)]'
#BPA__SELECT_DATE = '//input[@id ="mat-input-6"]'
BPA__SELECT_TIME = '//input[@id ="mat-input-7"]'
BPA__STC_DROPDOWN_FIELDS = ['Select Platform Model','Select Device Role','Select Release Software Version','File Transfer Protocol','Approval Status']
BPA__VIEW_CLICK = '/html/body/app-root/div/lib-joblisting/div[2]/div[2]/div/div/cisco-grid/div/ag-grid-angular/div/div[2]/div[1]/div[3]/div[2]/div/div/div[1]/div[11]/ng-component/a/mat-icon' 
BPA__ACTIVE_OS_UPGRADE = '//div[@class="mat-tab-label-content" and  text() = "Active Os Upgrade"]'
BPA__COMPLETE_OS_UPGRADE = '//div[@class="mat-tab-label-content" and  text() = "Completed Os Upgrade"]'
#BPA_SELECT_CREATE_NEW_XPATH = '//span[contains(text(), "Create New")]'
#BPA_SELECT_CREATE_NEW_XPATH = '//*[@id="gctDlgSaveBtn"]/button/span'
BPA__SELECT_MDT_ROWS = '//i[@class = "material-icons add-circle" and contains(text(),"add_circle")]'
BPA__SELECT_CREATE_NEW_XPATH = '//button[@class="btn btn--primary mat-button" ]//child::span[contains(text(), "Create New")]'
BPA__SELECT_NEW_FORM_XPATH_VALUES = '//mat-option//child::span[contains(text(), "{}")]'
BPA__CREATE_NEW_FORM_XPATH = '//div[@class="mat-select-value"]//child::span[text()= "{}"]'
BPA__SELECT_ARROW_LIST_XPATH = '/html/body/app-root/div/lib-osupgrade-order/div/div/div/div/form/div[1]/div/div[2]/div[1]/mat-form-field/div/div[1]/div/mat-select/div/div[2]/div'
BPA__SELECT_ARROW_LIST_DEVICE_ROLE_XPATH = '/html/body/app-root/div/lib-osupgrade-order/div/div/div/div/form/div[1]/div/div[2]/div[2]/mat-form-field/div/div[1]/div/mat-select/div/div[2]'
BPA__SELECT_OK_CONFIRMATION = '//button[@class = "btn btn--primary ng-star-inserted" and @id = "okButton"]'
BPA__MUTI_SELECT_XPATH = '//span[text()="Select Devices *"]'
BPA__MULTI_SELECT_XPATH_VALUES = '//div[@class= "ng-star-inserted"]//child::li[@class = "pure-checkbox ng-star-inserted"]//child::label[text()= "{}"]'
BPA_SELECT_MULTIPLE='/html/body/app-root/div/lib-osupgrade-order/div/div/div/div/form/div[1]/div/div[6]/div/div/div[4]/angular2-multiselect/div/div[2]/div[3]/div[4]/ul/li[1]/input'
#BPA__SELECT_PLATFORM_MODEL_XPATH = '/html/body/app-root/div/lib-osupgrade-order/div/div/div/div/form/div[1]/div/div[2]/div[1]/mat-form-field/div/div[1]/div/mat-select/div/div[1]/span'
#BPA__SELECT_DEVICE_ROLE_XPATH = '/html/body/app-root/div/lib-osupgrade-order/div/div/div/div/form/div[1]/div/div[2]/div[2]/mat-form-field/div/div[1]/div/mat-select/div/div[1]/span'
#BPA__SELECT_SOFTWARE_VER = '/html/body/app-root/div/lib-osupgrade-order/div/div/div/div/form/div[1]/div/div[3]/div[1]/mat-form-field/div/div[1]/div/mat-select/div/div[1]/span'
#BPA__SELECT_FILE_TRANSFER_PROTOCOL = '/html/body/app-root/div/lib-osupgrade-order/div/div/div/div/form/div[1]/div/div[3]/div[2]/mat-form-field/div/div[1]/div/mat-select/div/div[1]/span'
BPA__MDT_TXT_FIELD = '//input[@placeholder="MDT/TCN Number"]'
BPA_MDT_NEXT_TXT_FIELD = '/html/body/app-root/div/lib-osupgrade-order/div/div/div/div/form/div[1]/div/div[6]/div[2]/div/div[2]/mat-form-field/div/div[1]/div/input'
#BPA__SELECT_APPROVAL_STATUS = '/html/body/app-root/div/lib-osupgrade-order/div/div/div/div/form/div[1]/div/div[6]/div/div/div[3]/mat-form-field/div/div[1]/div/mat-select/div/div[1]/span'
BPA__SELECT_MULTIPLE_DEVICES = '/html/body/app-root/div/lib-osupgrade-order/div/div/div/div/form/div[1]/div/div[6]/div/div/div[4]/angular2-multiselect/div/div[1]/div/span[1]'
BPA__CREATE_NEW_SUBMIT = '/html/body/app-root/div/lib-osupgrade-order/div/div/div/div/form/div[2]/div[2]/button/span'
# Login page xpath information
BPA__TXT_UID_XPATH = '//input[@type="text" and @name="username"]'
BPA__TXT_PWD_XPATH = '//input[@type="password" and @name="password"]'
BPA__BTN_LOGIN_XPATH = '//button[@class="btn btn--primary"]'
BPA__LOADING_ICON_XPATH = '//div[@class="loading-icon ng-star-inserted"]'
BPA__LBL_DASHBOARD_XPATH = '//h5[contains(text(),"Dashboard")]//parent::div[@class="mdl-cell mdl-cell--3-col"]'
#BPA__MENU_PROFILE_XPATH = '//button[@class="menu-btn mdl-button mdl-button--icon"]//span[@class="mdl-button__ripple-container"]'  # BPA 2.1.1
BPA__MENU_PROFILE_XPATH = '//button[@class="new-user-icon mat-icon-button mat-primary"]//span[@class="mat-button-wrapper"]'  #STC OS LOgout
BPA__VERSION_XPATH = '//p[@class="versionText greyColorText"]'
BPA__CHECK_BPA_VERSION_URL = {"url": "/about/cisco-bpa-platform/mw-core"}
BPA__ABOUT_BPA = '//i[@id="openAboutDialogue"]'
BPA__CLOSE_ABOUT_BPA = '//button[@id="aboutCloseDialog"]'
BPA_VERSION_EXPR = '((\d+\.)*\d+)'
# Logout
#BPA__MENU_LOGOUT_XPATH = '//mdl-menu-item[@class="mdl-menu__item" and contains(text(),"Logout")]'
BPA__START_DATE_XPATH_REPORT = '/html/body/app-root/div/lib-joblisting/div[2]/div[1]/div/div/div[1]/div/mat-form-field/div/div[1]/div[2]/mat-datepicker-toggle/button'
BPA__START_DATE_VALUE = '//div[@class= "mat-calendar-body-cell-content" and text()="1"] '
BPA__END_DATE_XPATH_REPORT = '/html/body/app-root/div/lib-joblisting/div[2]/div[1]/div/div/div[2]/div/mat-form-field/div/div[1]/div[2]/mat-datepicker-toggle/button'
BPA__END_DATE_VALUE = '//div[@class= "mat-calendar-body-cell-content mat-calendar-body-today" ]'
BPA_JOB_STATUS_XPATH = '/html/body/app-root/div/lib-joblisting/div[2]/div[1]/div/div/div[3]/div/mat-form-field/div/div[1]/div/mat-select/div/div[2]'
BPA_JOB_STATUS_VALUE ='//span[@class= "mat-option-text" and contains(text(),"All")]'
BPA_DOWNLOAD_REPORT_XPATH ='/html/body/app-root/div/lib-joblisting/div[2]/div[1]/div/div/div[4]/button/span' 
BPA__MENU_LOGOUT_XPATH = '//button[contains(text(),"Logout")]'
BPA__TOAST_MSG = '//div[@class="toast-message ng-star-inserted"]'
BPA__TILE_FORMBUILDER_XPATH = '//h5[@class="parent-highlight top-20 new-label" and contains(text(),"Form Builder")]//ancestor::div[@class="mdl-cell mdl-cell--3-col show ng-star-inserted"]'
BPA__TILE_WORKFLOW_XPATH = '//h5[@class="parent-highlight top-20 new-label" and contains(text(),"Workflows")]//ancestor::div[@class="mdl-cell mdl-cell--3-col show ng-star-inserted"]'
BPA__TILE_DEVICEMANAGER_XPATH = '//h5[@class="parent-highlight top-20 new-label" and contains(text(),"Device Manager")]//ancestor::div[@class="mdl-cell mdl-cell--3-col show ng-star-inserted"]'
BPA__TILE_NETWORKTOPOLOGY_XPATH = '//h5[@class="parent-highlight top-20 new-label" and contains(text(),"Network Topology")]//ancestor::div[@class="mdl-cell mdl-cell--3-col show ng-star-inserted"]'
BPA__TILE_SERVICECENTER_XPATH = '//h5[@class="parent-highlight top-20 new-label" and contains(text(),"Service Center")]//ancestor::div[@class="mdl-cell mdl-cell--3-col show ng-star-inserted"]'
BPA__TILE_OSUPGRADE_XPATH = '//h5[@class="parent-highlight top-20 new-label" and contains(text(),"OS Upgrade")]//ancestor::div[@class="mdl-cell mdl-cell--3-col show ng-star-inserted"]'
BPA__TILE_PROCESSTEMPLATES = '//h5[@class="parent-highlight top-20 new-label" and contains(text(),"Process Templates")]//ancestor::div[@class="mdl-cell mdl-cell--3-col show ng-star-inserted"]'
BPA__LBL_BPA_XPATH = '//span[contains(text(),"Business Process Automation")]'
BPA__LBL_DEVICEMANAGER_XPATH = '//span[contains(text(),"Device Manager")]'
BPA__LBL_SERVICECENTER_XPATH = '//span[contains(text(),"Service Center")]'
BPA__LBL_PROCESS_TEMPLATE_XPATH = '//h5[@class="ng-star-inserted" and contains(text(),"Process Templates")]'
BPA__BTN_HOMEPAGE_XPATH = '//a[@id="homeButton" and @role="button"]'
# Form Builder
BPA__SERVICE_SELECTION_FORM_XPATH = '//mat-select[@id="serviceName"]'   # BPA 2.1.1
BPA__LBL_FRAMBUILDR_XPATH = '//span[contains(text(),"Form Builder")]'
BPA__TXT_SEARCH_XPATH = '//input[@placeholder="Search"]'
BPA__TXT_SEARCH_FROM_XPATH = '//input[@placeholder="From Date"]'
BPA__TXT_SEARCH_TO_XPATH = '//input[@placeholder="To Date"]'
BPA__BTN_SEARCH_FORM_XPATH = '//button[@class="btn btn--small btn--icon btn--white"]//child::span[@title="Search"]'  # BPA 2.1.1
BPA__NSO = "nso"
BPA__EDIT_FORM_TEXTFEILD_XPATH = '//input[@placeholder="{}"]'  # BPA 2.1.1
BPA__EDIT_FORM_DROPDOWN_XPATH = '//mat-select[@placeholder="{}"]'  # BPA 2.1.1
BPA__EDIT_FORM_OPTION_XPATH = '//div[@class="mat-select-content ng-trigger ng-trigger-fadeInContent"]//child::mat-option[@role="option"]//child::span[@class="mat-option-text" and contains(text(), "{}")]'  # BPA 2.1.1
BPA__EDIT_FORM_CHOICE_FIELD_XPATH = '//div[@class="padding-10 col-sm-12"]//label[@class="formBuildLabel ng-star-inserted" and contains(text(), "{}")]'  # BPA 2.1.1
BPA__SERVICE_NAME = "service_name"
BPA__EDIT_NSO_XPATH = '//div[@class="mat-select-value"]//parent::div//parent::mat-select[@id="selectedNso"]'
BPA__SELECT_EDIT_NSO_XPATH = '//span[text()="{}"]//parent::span[@class="mat-option-text"]'
BPA__SERVICE_NAME_XPATH = '//div[@class="mat-select-value"]//parent::div//parent::mat-select[@name="serviceName"]'
BPA__SELECT_SERVICE_NAME_XPATH = '//span[@class="mat-option-text"][text()="{}"]'
BPA__CONTINUE_BTN_XPATH = '//button[text()="Continue"]'
BPA__CONFIGURE_BUTTON = '//label[text()="{}"]//preceding-sibling::i[@class="config-btn"]//child::mat-icon[text()="settings"]'
BPA__INFO_XPATH = '//*[@id]//mat-form-field//input[@placeholder="Info"]'
BPA__EXPLORE_BUTTON = '//label[text()="{}"]//preceding-sibling::i[@class="config-btn ng-star-inserted"]//child::mat-icon[text()="launch"]'
BPA__ELEMENT_OK_XPATH = "//span[contains(@class,'mat-button-wrapper') and text() = 'Ok']"
BPA__ICON_DELETE_FROM_XPATH = '//a[@class="blue-icon btn-xs ng-star-inserted" and @mat-tooltip="Delete"]'
BPA__ICON_EDIT_FROM_XPATH = '//a[@class="blue-icon btn-xs ng-star-inserted" and @mat-tooltip="Form Designer"]'
BPA__BTN_CONFIRM_FORM_XPATH = '//*[@id="cdk-overlay-1"]/mat-dialog-container/app-confirm/div/div/div[2]/button[1]'
BPA__EDIT_FORM_XPATH = '//h5[contains(text(),"(Create/Edit) Form")]'
BPA__UPLOAD_FORM_XPATH = '//input[@type="file" and @accept=".json"]'  # BPA 2.0
BPA__DIALOG_CONFIRM_FORM_XPATH = '//div[@class="cdk-overlay-pane"]'
BPA__BTN_OK_XPATH = '//button[@id="okButton" and contains(text(),"Ok")]'
BPA__BTN_CANCEL_XPATH = '//button[@id="cancelButton" and contains(text(),"Cancel")]'
BPA__SAVE_FORM_XPATH = '//span[contains(@class,"mat-button-wrapper") and text() = "Save"]'
BPA__SELECT_FORM_XPATH = '//div[@col-id="name" and text()="%s"]//preceding::div[@class="ag-cell ag-cell-not-inline-editing ag-cell-with-height ag-cell-last-left-pinned ag-cell-no-focus"]//child::span[@class="ag-icon ag-icon-checkbox-unchecked"]'
BPA__BTN_FORM_DELETE_XPATH = '//button[@id="deleteForms" and @mattooltip="Delete Multiple Forms"]'
# Workflow
BPA__config_text_label = "//label[text()=\""
BPA__config_btn = "\"]//parent::div[@class= 'form-group']//following-sibling::i[@class= 'config-btn']"
BPA__info_field_holder = "//*[@id]//mat-form-field//input[@placeholder=\'"
BPA__closing_bracket = "\']"
BPA__explore_btn = "\"]//parent::div[@class= 'form-group']//following-sibling::i[@class= 'config-btn' and @mattooltip = 'Explore']"
BPA__workflow_tab = "/html/body/app-root/div/app-home/div/div[1]/mdl-card/mdl-card-supporting-text/div[2]/div[8]/div"
BPA__defined_workflow_tab = "/html/body/app-root/div/app-header/div[1]/div/div/nav/div/a[3]"
BPA__workflow_instance_tab = "/html/body/app-root/div/app-header/div[1]/div/div/nav/div/a[4]/span"
BPA__workflow_add_btn = "/html/body/app-root/div/app-defined-processes/div/div/div/div[1]/div[3]/button"
BPA__workflow_file_upload_btn = "//*[@id= 'mat-step-content-0-0']/mat-card/mat-card-content/section[1]/section[1]/input"
BPA__workflow_deploy_all_btn = "//button[contains(text(), 'Deploy All')]"
BPA__workflow_grp_select = "//*[@id= 'mat-select-1']/div/div[2]"
BPA__workflow_grp_chkbx_start = "//span[@class= 'mat-option-text'][./text()= '"
BPA__workflow_closing = "']"
BPA__workflow_div_outside = "//*[contains(text(), 'Select Group & Permission')]"
BPA__workflow_perm_chkbx_start = "//span[@class= 'mat-checkbox-label'][./text()= '"
BPA__workflow_submit_btn = "//*[@id= 'mat-step-content-0-1']/mat-card/mat-card-actions/button[2]"
BPA__workflow_close_btn = "//*[@id= 'mat-step-content-0-1']/mat-card/mat-card-actions/button[3]/span"
BPA__workflow_instance_tab = "/html/body/app-root/div/app-header/div[1]/div/div/nav/div/a[4]/span"
BPA__create_workflow_groups = ["svcacct", "device-manager", "service-manager"]  # BPA 2.1.1
BPA__create_workflow_permissions = ["Select All"]
BPA__WORKFLOW_VIEWTASK_TASKLIST_XPATH = '//a[@title="View and Claim Form"]'
BPA__WORKFLOW_VIEW_TASK_XPATH = '//div[contains(text(),"%s")]//following-sibling::div[@col-id="Actions"]//child::a[@data-original-title="View task"]'
BPA__BTN_CONTINUE_WORKFLOW_TASKLIST_XPATH = '//span[contains(text(),"Continue")]//parent::button[@id="button0"]'
BPA__BTN_COMPLETE_WORKFLOW_TASKLIST_XPATH = '//button[@class="btn btn--primary mat-button ng-star-inserted"]//child::span[contains(text(),"Complete")]'
BPA__BTNOK_WORKFLOW_TASKLIST_XPATH = '//button[@class="mdl-button btn btn--primary mat-button"]//child::span[contains(text(),"Ok")]'
BPA__LBL_DEFINED_WORKFLOW_XPATH = '//span[contains(text(),"Defined Workflows")]'
BPA__TAB_TASKS_WORKFLOW_XPATH = '//span[@class = "ng-star-inserted" and text() = "Tasks"]'
BPA__VIEW_TASK_WORKFLOW_XPATH = '//div[contains(text(),"{}")]//following-sibling::div[@col-id="Actions"]//child::a[@data-original-title="View Form"]'
BPA__TAB_DEFINED_WORKFLOW_XPATH = '//a[@class="mdl-navigation__link new-tab mat-tab-link ng-star-inserted" and @href="/workflow/defined-processes"]//child::span[@class="ng-star-inserted"]'
BPA__TAB_WORKFLOW_INSTANCE_XPATH = '//a[@class="mdl-navigation__link new-tab mat-tab-link ng-star-inserted" and @href="/workflow/instances"]'
BPA__BTN_ADD_WORKFLOW_XPATH = '//button[contains(text(),"Import") and @mattooltip="Import Process Definition"]'  # BPA 2.1.1
BPA__DELETE_MULTIPLE_WORKFLOWS = '//div[text() = "{}"]//parent::div[@role="row"]//child::a[@data-original-title="{}"]'
BPA__DELETE_WORKFLOW_FOR_MULTIPLE_VERSIONS = '//div[text() = "{}"]//parent::div[@role="row"]//child::a[@data-original-title="{}"]'
BPA__MULTIPLE_ACTIONS_FOR_SINGLE_WORKFLOW = '//div[contains(text(),"{}")]//following-sibling::div[text() = "{}"]//parent::div[@role="row"]//child::a[@data-original-title="{}"]'
BPA__DELETE_ACTIVITY = 'Delete'
BPA__VIEW_ACTIVITY = 'View detail'
BPA__EDIT_ACTIVITY = 'Edit'
BPA__EDIT_FORM_ACTIVITY = 'Form Designer'
BPA__START_ACTIVITY = 'Start'
BPA__BTN_EDIT_WORKFLOW = 'Edit diagram'
BPA__BTN_DOWNLOAD_WORKFLOW = 'Download'
BPA__BTN_START_CONFIRM = '//button[@id="startButton"]'
BPA__DOWNLOAD_ACTIVITY = 'Download'
BPA__CLOSE_TOAST_MSG = '//button[@aria-label = "Close"]'
BPA__BTN_FILE_UPLOAD_WORKFLOW_XPATH = '//input[@id="bpmnFiles" and @type="file"]'
BPA__BTN_DEPLOY_ALL_WORKFLOW_XPATH = '//button[contains(text(), "Deploy All")]'
BPA__WORKFOW_GROUP_SELECT_XPATH = '//span[contains(text(),"Select Groups")]'
BPA__WORKFOW_GROUP_DIV_OUTSIDE_XPATH = "//*[contains(text(), 'Select Group & Permission')]"
BPA__WORKFOW_GROUP_CHECKBOX_START = '//span[text()="%s"]//ancestor::mat-option[@role="option"]//child::mat-pseudo-checkbox'
BPA__CHK_WORKFLOW_PERMISSON_XPATH = "//span[@class= 'mat-checkbox-label'][./text()= '{}']"
BPA__BTN_WORKFLOW_SUBMIT_XPATH = '//button[@id="submitButton" and contains(text(),"Submit")]'
BPA__BTN_WORKFLOW_CLOSE_XPATH = '//button[@id="submitButton"]//following::button[@id="closeButton"]'
BPA__TXT_WORKFLOW_SEARCH_XPATH = '//input[@placeholder="Search"]'
BPA__BTN_SEARCH_WORKFLOW_XPATH = '//button[@class="btn btn--small btn--icon btn--white"]//child::span[@title="Search"]'  # bpa 2.1.1
BPA__LBL_WORKFLOW_INSTANCE_XPATH = '//h3[contains(text(), "Workflow Instances")]'
BPA__LBL_WORKFLOW_XPATH = '//h3[contains(text(),"Workflows")]'
BPA__BTN_START_WORKFLOW_XPATH = '//button[@class="btn btn--primary mat-button"]'
BPA__BTN_START_CONFIRM_OK_WORKFLOW_XPATH = '//button[@class="btn btn--primary mat-button"and @aria-label="Close dialog"]'
BPA__TXT_SEARCH_WORKFLOW_INSTANCE_XPATH = '//mat-select[@placeholder="Select Process Instance Type" and @role="listbox"]'
BPA__TXT_FROMDATE_WORKFLOW_INSTANCE_XPATH = '//input[@placeholder="From Date"]'
BPA__TXT_TODATE_WORKFLOW_INSTANCE_XPATH = '//input[@placeholder="To Date"]'
BPA__TXT_SEARCH_WORKFLOW_XPATH = '//input[@placeholder="Search"]'
BPA__TXT_SEARCH_TASK_WORKFLOW_XPATH = '//input[@placeholder="Filter"]'
BPA__LBL_PROCESSID_TASK_WORKFLOW_XPATH = '//span[contains(text(),"Process Instance ID")]'
BPA__WORKFLOW_DELETE_YES_XPATH = '//button[@class="btn btn--primary"][contains(text(), "Ok")]'  # bpa 2.1.1
BPA__WORKFLOW_DELETE_ALL_VERSIONS_XPATH = '//td[text()="%s"]/following-sibling::td//parent::tr//following-sibling::a[@mattooltip="Delete"]'
BPA__WORKFLOW_SEARCH_XPATH = '//*[@id="mat-input-0"]'
BPA__WORKFLOW_NEXT_PAGE_XPATH = ' /html/body/app-root/div/app-defined-processes/div/div/div/div[2]/div/div/div/mat-paginator/button[2]'
BPA__WORKFLOW_EXECUTE_XPATH = '//div[contains(text(),"%s")]//following-sibling::div[contains(text(), "%s")]//parent::div[@role="row"]//child::a[@data-original-title="Start"]'  # bpa 2.1.1
BPA__WORKFLOW_DELETE_VERSION_XPATH = '//div[contains(text(),"%s")]//following-sibling::div[contains(text(), "%s")]//parent::div[@role="row"]//child::a[@data-original-title="Delete"]'
BPA__WORKFLOW_VERSIONS_XPATH = '//td[contains(text(), "%s")]//following-sibling::td[1]'
BPA__WORKFLOW_CONFIRM_XPATH = '//div[@class="confirmation-dialog"]'
BPA__TXT_WORKFLOW_EDIT_JSON_XPATH = '//div[@class="mat-form-field-infix"]//child::input[@placeholder="%s"]'
BPA__LIST_WORKFLOW_EDIT_JSON_XPATH = '//div[@class= "selected-list"]'
BPA__LISTITEM_WORKFLOW_EDIT_JSON_XPATH = '//div[@class="ng-star-inserted"]//ancestor::label[contains(text(), "%s")]'
BPA__WORKFLOW_SERVICE_INPUT = '//div[@class = "mdl-grid"]//child::h5[contains(text(), "Service Input")]'
BPA__WORKFLOW_SINGLE_ICON_ACTIVITY_XPATH = '//div[contains(text(),"{}")]//following-sibling::div[text() = "{}"]//following-sibling::div[text() = "{}"]//parent::div[@role="row"]//child::a[@data-original-title="{}"]'
BPA__WORKFLOW_EDIT_TEXT_FIELD = '//div[@class="bpp-field-wrapper"]//child::input[@name="%s"]'
BPA__WORKFLOW_DEPLOY_BTN = '//button[@class="btn btn--primary" and contains(text(), "Deploy")]'
BPA__IMPORT_WORKFLOW_AS_DRAFT = '//button[@id="importWorkflowDraftButton"]'
BPA__SAVE_AS_DRAFT_BTN = '//button[@id= "deployAllButton"]'
BPA__UPLOAD_WORKFLOW_DRAFT_CLOSE_BTN = '//button[@id="closeButton"]'
BPA__CREATE_WORKFLOW_NAME = '//input[@id = "workflowName"]'
BPA__CREATE_KEY = '//input[@id = "key"]'
BPA__CREATE_WORKFLOW_PROCEED = '//button[@id= "startButton"]'
BPA__CREATE_WORKFLOW_BTN = '//button[@id= "addWorkflowButton"]'
BPA__WORKFLOW_SINGLE_SELECT_XPATH = '//div[contains(text(),"{}")]//following-sibling::div[contains(text(),"{}")]//following-sibling::div[contains(text(), "{}")]//parent::div[@role="row"]'
# DEVICE MANAGER
BPA__TXT_DEVICE_MANAGER_SEARCH_XPATH = '//input[@class="mat-input-element mat-form-field-autofill-control ng-untouched ng-pristine ng-valid" and @placeholder="Search"]'
BPA__BTN_DELETE_DEVICE_XPATH = '//*[@class="mat-icon material-icons" and contains(text(),"delete")]'
BPA__BTN_DELETE_CNFRM_OK_DEVICE_MGR_XPATH = '//*[@class="btn btn--primary"  and contains(text(),"Ok")]'
BPA__CLICK_NSO_XPATH = '//mat-select[@placeholder="Select NSO" and @role="listbox"]'
BPA__SELECT_NSO_XPATH = '//span[@class="mat-option-text"]//child::span[text()= "{}"]'
BPA__SEARCH_DEVICE_XPATH = '//*[@id="mat-input-0"]'
BPA__EDIT_DEVICE_TEXT_XPATH = '//input[@placeholder="{}"]'
BPA__EDIT_DEVICE_DROPDOWN_XPATH = '//mat-select[@aria-label="{}"]'
BPA__EDIT_DEVICE_DROPDOWN_OPTION_XPATH = '//mat-option//child::span[contains(text(), "{}")]'
BPA__BTN_DELETE_DEVICE_XPATH = '//div[text()="{}"]//following-sibling::div//child::a[@mat-tooltip="Delete"]'
BPA__BTN_DELETE_CNFRM_OK_DEVICE_MGR_XPATH = '//*[@id="okButton" and contains(text(),"Ok")]'
BPA__LBL_DEVICE_TEXT = '//div[text()="{}"]'
BPA__VIEW_DEVICE_XPATH = '//div[text()="{}"]//following-sibling::div//child::a[@mat-tooltip="View detail"]'
BPA__VIEW_DEVICE_NAME_XPATH = '//div[@class="label-content"][text()="{}"]'
BPA__VIEW_DEVICE_CLOSE_XPATH = '//button[@class="mdl-dialog__close mdl-button mdl-button--icon"]'
BPA__SEARCH_XPATH = '//input[@placeholder="Search"]'
BPA__SEARCH_CLICK_XPATH = '//button[@class="btn btn--small btn--icon btn--white"]'
BPA__EDIT_DEVICE_XPATH = '//div[text()="{}"]//following-sibling::div//child::a[@mat-tooltip="Edit"]'
BPA__EDIT_DEVICE_TEXT_FIELD_NAMES = ['Address', 'Port', 'Description', 'Latitude', 'Longitude']
BPA__EDIT_DEVICE_DROPDOWN_FIELD_NAMES = ['Select Auth Group', 'Admin State', 'Select Device-Type', 'Ned Id']
BPA__EDIT_DEVICE_OK_XPATH = '//span[contains(text(), "Ok")]'
BPA__ADD_DEVICE_XPATH = '//button [@mattooltip="Add Device"]'
BPA__ADD_DEVICE_TEXT_FIELD_NAMES = ['Name', 'Address', 'Port', 'Description', 'Latitude', 'Longitude']
BPA__ADD_DEVICE_POPUP_XPATH = '//div[@id="dmDialogHeading"][text()[contains(., "Add Device")]]'
BPA__LOGOUT_BUTTON = '//span[@class="mdl-button__ripple-container"]'
BPA__EDIT_DEVICE_POPUP_XPATH = '//div[@id="dmDialogHeading"][text()[contains(.,"Edit Device")]]'

# SERVICE CENTER
BPA__SERVICE_LIST_DRPDWN_XPATH = '//input[@id="selectedServices"]'
BPA__DEVICE_NAME_DROP_DOWN_XPATH = '//div[@class="mat-select-value"]//span[text()="device-name"]'
BPA__DEVICE_NAME_SELECTION_XPATH = '//mat-option//span[text()="{}"]'
BPA__SELECT_SERVICE_DRPDWN_OPTION_XPATH = '//span[contains(text()," Dummy-service-package-2:Dummy-service-package-2 ")]'
BPA__TXT_SEARCH_XPATH = '//input[@placeholder="Search"]'
BPA__TXT_SEARCH_FROM_XPATH = '//input[@placeholder="From Date"]'
BPA__TXT_SEARCH_TO_XPATH = '//input[@placeholder="To Date"]'
BPA__DELETE_SERVICE_XPATH = '//div[text()="{}"]//following-sibling::div[@col-id="Actions"]//child::a[@mat-tooltip="Delete"]'
BPA__DELETE_SERVICE_CONFM_BUTTON = '//button[@id="okButton" and contains(text(),"Ok")]'
BPA__EDIT_SERVICE_XPATH = '//div[text()="{}"]//following-sibling::div[@col-id="Actions"]//child::a[@mat-tooltip="Edit"]'
BPA__EDIT_TEXT_FEILD_XPATH = '//input[@placeholder="{}"]'
BPA__EDIT_SERVICE_FORM_XPATH = '//h5[@class="ng-star-inserted" and contains(text(),"Service Center")]'
BPA__DROP_DOWN_LIST_XPATH = '//div[@class="selected-list"]//child::span[text()="{}"]'
BPA__DROP_DOWN_LIST_XPATH2 = '//label[text()="{}"]//ancestor::li[@class="pure-checkbox ng-star-inserted"]'
BPA__DROP_DOWN_SELECT_ALL = '//span[text()="Select All"]//ancestor::div[@class="pure-checkbox select-all ng-star-inserted"]'
BPA__SERVICE_COMMIT_BTN_XPATH = '//button[@id="commitInstanceBtn"]'
BPA__DELETE_BTN_XPATH = '//button[@id="dltBtnServiceInstance" and contains(text()," Delete ")]'
BPA__BTN_COMMIT_OK_SERVICE_CENTER_XPATH = '//button[text()="Ok"]'
BPA__BTN_REVERT_OK_SERVICE_CENTER_XPATH = '//button[text()="Ok"]'
BPA__BTN_CONFIRM_DELETE_WORKFLOW_XPATH = '//button[text()="Ok"]'
BPA__UPLOAD_SERVICE_XPATH = '//input[@type="file" and @accept=".json"]'   # BPA 2.0
BPA__LBL_SERVICECENTER_XPATH = '//span[contains(text(),"Service Center")]'
BPA__NSO_DROPDOWN_XPATH = '//mat-select[@aria-label="Select NSO"]'
BPA__TXT_SERVICE_LIST_XPATH = '//mat-select[@id="selectedServices"]'      # bpa 2.1.1
BPA__SELECT_SERVICE_LIST_XPATH = '//span[contains(text(),"{}")]//ancestor::mat-option'
BPA__NSO_DROPDOWN_SELECT_XPATH = '//span[text()="{}"]//ancestor::mat-option'
BPA__BTN_ADD_SERVICE_CENTER_XPATH = '//button[@mattooltip= "Add New Instance"]'
BPA__BTN_UPLOAD_SERVICE_CENTER_XPATH = '//button[@mattooltip="Import Instance"]'
BPA__BTN_DOWNLOAD_SERVICE_CENTER_XPATH = '//button[@mattooltip="Download Instances"]'
BPA__BTN_DELETE_SERVICE_CENTER_XPATH = '//button[@mattooltip="Download Instances"]'
BPA__BTN_DOWNLOAD_CSV_SERVICE_CENTER_XPATH = '//button[contains(text(),"CSV")]'
BPA__BTN_DOWNLOAD_EXCEL_SERVICE_CENTER_XPATH = '//button[contains(text(),"Excel")]'
BPA__DROPWDOWN_COMMIT_DR_FORMAT_SELECT_XPATH = '//span[@style]//parent::div[@class="mat-select-value"]//following-sibling::div[@class="mat-select-arrow-wrapper"]//child::div[@class="mat-select-arrow"]'
BPA__DROPWDOWN_COMMIT_DR_FORMAT_SELECT_XML_XPATH = '//span[contains(text(),"xml")]//ancestor::mat-option'
BPA__BTN_CLOSE_COMMIT_DR_SERVICE_CENTER_XPATH = '//mdl-icon[text()="close"]//parent::button[@aria-label="Close dialog"]'
BPA__BTN_COMMIT_DRY_RUN_SERVICE_CENTER_XPATH = '//button[@id="commitDRInstanceBtn"]'
BPA__BTN_COMMIT_SERVICE_CENTER_XPATH = '//button[@id="commitInstanceBtn"]'
BPA__BTN_COMMIT_DROPDOWN_SERVICE_CENTER_XPATH = '//button[@id="commit-queue-options"]'
BPA__BTN_COMMIT_OPTION_SERVICE_CENTER_XPATH = '//button[@class="mat-menu-item" and text() = "{}"]'
BPA__TXT_ADD_NAME_SERVICE_CENTER_XPATH = '//input[@placeholder="name"]'
BPA__BTN_NEXT_ADD_SERVICE_CENTER_XPATH = '//div[@class="mdl-dialog__actions"]//child::button[text()="Next"]'
BPA__BTN_ADD_CLOSE_SERVICE_CENTER_XPATH = '//mdl-icon[text()="close"]//parent::button'
BPA__BTN_ADD_COMMIT_OK_SERVICE_CENTER_XPATH = '//button[text()="Ok"]'
BPA__BTN_REVERT_SERVICE_XPATH = '//button[@id="instanceRevertBtn"]'
BPA__CHKBOX_SELECT_ALL_SERVICE_CENTER_XPATH = '//span[@class="ag-header-select-all" and @ref="cbSelectAll"]'
BPA__UPLOAD_SERVICE_CENTER_XPATH = '//input[@type="file" and @accept=".json"]'  # BPA 2.0
BPA__BTN_VIEW_SERVICE_CENTER_XPATH = '//div[text()="{}"]//following-sibling::div[@col-id="Actions"]//child::a[@mat-tooltip="View detail"]'
BPA__CHKBOX_OPTION_SERVICE_CENTER_XPATH = '//div[@class="ag-pinned-left-cols-container"]//div[@row-id="{}"]//span[@class="ag-icon ag-icon-checkbox-unchecked"]'
BPA__SERVICE_NAME_SERVICE_CENTER_XPATH = '//div[contains(text(), "{}")]//parent::div[@tabindex="-1"]//parent::div[@role="row"]'

# Process Templates
BPA__TEMPLATE_ADD_SELECT_DEVICE = '//span[text()="Select Device"]'  # BPA 2.1.1
BPA__EDIT_SELECT_DEVICE_OPTION_XPATH = '//label[text() = "{}"]'     # BPA 2.1.1
BPA__TXT_FROMDATE_PROCESSTEMPLATES_XPATH = '//input[@placeholder="From Date"]'
BPA__TXT_TODATE_PROCESSTEMPLATES_XPATH = '//input[@placeholder="To Date"]'
BPA__TXT_SEARCH_PROCESSTEMPLATES_XPATH = '//input[@placeholder="Search"]'
BPA__UPLOAD_PROCESSTEMPLATES_XPATH = '//input[@type="file" and @accept="{}"]'                  # BPA 2.0
BPA__UPLOAD_FILE_XPATH = '//input[@type="file" and @accept="{}"]'                              # BPA 2.1.1
BPA__ADD_TEMPLATE_POPUP_XPATH = '//input[@id="ptTemplateName"]'
BPA__ADD_TEMPLATE_TEXT_FIELD_NAMES = ['Name', 'Description', 'Pass Criteria']
BPA__EDIT_TEMPLATE_TEXT_XPATH = '//input[@placeholder="{}"]'
BPA__BTN_ADD_TEMPLATE = '//button[@class="btn btn--primary" and contains(text(),"Add")]'       # BPA 2.1.1
BPA__BTN_ACTIVITY_TEMPLATE = '//button[contains(text(),"%s")]'
BPA__EDIT_TEMPLATE_DROPDOWN_FIELD_NAMES = ['Select NSO', 'Select NED']                         # BPA 2.1.1
BPA__EDIT_TEMPLATE_DROPDOWN_XPATH = '//mat-select[@aria-label="{}"]'                           # BPA 2.1.1
BPA__EDIT_TEMPLATE_DROPDOWN_OPTION_XPATH = '//mat-option//child::span[contains(text(),"{}")]'  # BPA 2.1.1
BPA__TEMPLATE_ADD_COMMAND = '//mat-expansion-panel[@id="ptCommand0"]'
INPUT_COMMAND_XPATH = '//input[@placeholder="Command"]'
BPA__TEMPLATE_NAME_XPATH = '//div[text()="{}"]//parent::div[@role="row"]'
BPA__SINGLE_ICON_ACTIVITY_XPATH = '//div[text()="{}"]//parent::div[@role="row"]//child::a[@data-original-title="{}"]'
BPA__BTN_TEST_TEMPLATE_XPATH = '//button[@id="ptTestTemplateForm"]'
BPA__ADD_TEMPLATE_TEST_CONFIRM_XPATH = '//mat-card-title[@class = "mat-card-title"]'
# scripts
BPA__SCRIPTS_BTN_xpath = '//a[@id="item4"]'
BPA__SCRIPTS_ADD_xpath = '//button[@id="addScript"]'
BPA__SCRIPTS_ADD_POPUP_XPATH = '//input[@id="command"]'
BPA__SCRIPTS_ADD_DROPDOWN_FIELD_XPATH = ['Type *']
BPA__SCRIPTS_ADD_TEXT_FIELD_NAME_XPATH = ['command']
BPA__SCRIPTS_ADD_EDIT_TEXT_XPATH = '//input[@id="{}"]'
BPA__SCRIPTS_ADD_EDIT_DROPDOWN_XPATH = '//mat-select[@placeholder="{}"]'
BPA__SCRIPTS_ADD_EDIT_OPTION_XPATH = '//mat-option//child::span[text()="{}"]'
BPA__SCRIPTS_ADD_SELECT_FILE_XPATH = '//input[@id="scriptUploadReal"]'
BPA__SCRIPTS_ADD_SAVE_BTN_xpath = '//button[@id="saveButton"]'
BPA__VIEW_CLOSE_BTN = '//button[@aria-label="Close dialog"]'
# analytics
BPA__ANALYTICS_TAB_XPATH = '//span[@class="ng-star-inserted" and text()="Analytics"]'
BPA__ANALYTICS_ADD_XPATH = '//button[@id ="ptAddATBtn"]'
BPA__ADD_PROCESS_TEXT_FIELD_NAMES = ['ID']
BPA__EDIT_PROCESS_DROPDOWN_FIELD_NAMES = ['Choose First Template', 'Choose Second Template']
BTN_SAVE_UPDATE_ANALYTICS = '//button[@class = "btn btn--primary ng-star-inserted"]'
# executions
BPA__EXECUTION_TAB_XPATH = '//span[@class="ng-star-inserted" and text()="Executions"]'
BPA__EXECUTION_CLEAR_BTN = '//span[@id="clearButton"]'
BPA__EXECUTION_CLOSE_BTN = '//button[@id = "ptCloseViewBtn"]'
BPA__EXECUTION_SELECT_ALL_BTN = '//div[@class="ag-pinned-left-header"]//span[@ref="cbSelectAll"]'
BPA__EXECUTION_VIEW_ICON = '//mat-icon[text() = "remove_red_eye"]'
# Search with date
BPA__START_DATE_XPATH = '//input[@id="ptStartDate"]'
BPA__START_DATE_BACKGROUND_XPATH = '//div[@class="cdk-overlay-container"]'
BPA__END_DATE_XPATH = '//input[@id="ptEndDate"]'
BPA__END_DATE_BACKGROUND_XPATH = '//div[@class="cdk-overlay-backdrop mat-overlay-transparent-backdrop cdk-overlay-backdrop-showing"]'
BPA__HEADER_XPATH = '//header[@class="mdl-layout__header mdl-layout--fixed-header"]'
