# Python imports
import logging

# Core Django imports
from django.shortcuts import render
from django.shortcuts import redirect

logger = logging.getLogger(__name__)

def mail_send(request):
    if request.method == "GET":
        context = {'page_title': "Mail send, Input"}
        context['page_summary_text'] = "Please fill the form"
        logger.debug('DEBUB Got a request for mail_send view with the GET verb')
        return render(request, 'paws/f_mail_send.html', context)
    if request.method == "POST":
        form_data = request.POST
        context = {'page_title': "Mail send, Output"}
        try:
            mail_to = form_data['mail_to']
            mail_subject = form_data['mail_subject']
            mail_body = form_data['mail_body']
            context['page_summary_text'] = "Outcome of sending mail to " + mail_to + " with subject " + mail_subject
            logging.debug("mail_to, mail_subject, mail_body" + mail_to + mail_subject +  mail_body)
            from paws.libs.mail import mail_verbs
            mail_from = 'noreply@white.heanet.ie'
            mail_message = mail_verbs.mail_send(mail_from, mail_to, mail_subject, mail_body)
            logging.debug("Outcome of view mail_send in paws app is: " + mail_message)
            context['text_message'] = mail_message
            return render(request, 'paws/r_text.html', context)
        except Exception as err:
            my_error = "WARNING, the following error has happened: " + str(err)
            context['page_summary_text'] = "The following error has happened: "
            context['text_message'] = str(err)
            return render(request, 'paws/r_text.html', context)


def clientdb_client_one(request):
    if request.method == "GET":
        context = {'page_title': "ClientDB client detail, Input"}
        context['page_summary_text'] = "Please enter a ClientDB client_id"
        logger.debug('DEBUB Got a request for clientdb_client_one view with the GET verb')
        return render(request, 'paws/f_clientdb_client_one.html', context)
    if request.method == "POST":
        form_data = request.POST
        context = {'page_title': "ClientDB client detail, Output"}
        try:
            from paws.libs.clientdb import clientdb_get_client_one
            client_id = form_data['field_in']
            client = clientdb_get_client_one.clientdb_client_one_tech(client_id)
            context['page_summary_text'] = "These are the details of the ClientDB client"
            context['text_message'] = client
            context['list_to_render'] = client
            return render(request, 'paws/r_list.html', context)
        except Exception as err:
            my_error = "WARNING, the following error has happened: " + str(err)
            context['page_summary_text'] = "The following error has happened: "
            context['text_message'] = str(err)
            return render(request, 'paws/r_text.html', context)

def csd_customer_one(request):
    if request.method == "GET":
        context = {'page_title': "CSD customer detail, Input"}
        context['page_summary_text'] = "Please enter a CSD customer Identity"
        logger.debug('DEBUB Got a request for csd_customer_one view with the GET verb')
        return render(request, 'paws/f_csd_customer_one.html', context)
    if request.method == "POST":
        form_data = request.POST
        context = {'page_title': "CSD customer detail, Output"}
        try:
            from paws.libs.csd import csd_get_customer_one_detail
            customer_id = form_data['field_in']
            customer = csd_get_customer_one_detail.csd_customer_detail(customer_id)
            context['page_summary_text'] = "These are the details of the CSD customer"
            context['dict_to_render'] = customer
            context['text_message'] = customer
            return render(request, 'paws/r_dict.html', context)
        except Exception as err:
            my_error = "WARNING, the following error has happened: " + str(err)
            context['page_summary_text'] = "The following error has happened: "
            context['text_message'] = str(err)
            return render(request, 'paws/r_text.html', context)


def csd_eline_one(request):
    if request.method == "GET":
        context = {'page_title': "ELINE detail, Input"}
        context['page_summary_text'] = "Please enter a CSD service Identity"
        logger.debug('DEBUB Got a request for csd_eline_one view with the GET verb')
        return render(request, 'paws/f_csd_eline_one.html', context)
    if request.method == "POST":
        form_data = request.POST
        context = {'page_title': "ELINE detail, Output"}
        try:
            from paws.libs.csd import csd_get_eline_one_detail
            eline_identity = form_data['field_in']
            #print("Next is the eline_identity as received in the POST of view csd_eline_one")
            #print(eline_identity)
            eline = csd_get_eline_one_detail.csd_eline_detail(eline_identity)
            #print("Next is from invoking csd_eline_detail from the paws view")
            #print(eline)
            context['page_summary_text'] = "These are the details of the ELINE"
            context['dict_to_render'] = eline
            context['text_message'] = eline
            return render(request, 'paws/r_dict.html', context)
        except Exception as err:
            my_error = "WARNING, the following error has happened: " + str(err)
            context['page_summary_text'] = "The following error has happened: "
            context['text_message'] = str(err)
            return render(request, 'paws/r_text.html', context)



def csd_eline_all_fault(request):
    if request.method == "GET":
        context = {'page_title': "ELINE by fault status, Input"}
        context['page_summary_text'] = "Give a fault status ('Up', 'Down' or 'None' withouth the '') and will tell you what services are in that status"
        logger.debug('DEBUB Got a request for csd_eline_all_fault view with the GET verb')
        return render(request, 'paws/f_csd_eline_all_fault.html', context)
    if request.method == "POST":
        form_data = request.POST
        context = {'page_title': "ELINE by fault status, Output"}
        try:
            from paws.libs.csd import csd_get_eline_all_by_fault_status
            fault_status = form_data['field_in']
            #elines = csd_get_eline_all_by_fault_status.csd_elines_by_fault_status('None')
            elines = csd_get_eline_all_by_fault_status.csd_elines_by_fault_status(fault_status)
            #print("Next is from invoking csd_elines_by_fault_status from the paws View")
            #print(elines)
            context['page_summary_text'] = "These are the ELINE 'Identity' in fault_status: " + fault_status
            context['list_to_render'] = elines
            context['text_message'] = elines
            return render(request, 'paws/r_list.html', context)
        except Exception as err:
            my_error = "WARNING, the following error has happened: " + str(err)
            context['page_summary_text'] = "The following error has happened: "
            context['text_message'] = str(err)
            #return redirect('core:about')
            return render(request, 'paws/r_text.html', context)



def saint2year(request):
    if request.method == "GET":
        context = {'page_title': "Saint to Year, Input"}
        context['page_summary_text'] = "This is what I do: You give me a Saint and I will give you his/her birth year."
        logger.debug('DEBUB Got a request for saint2year view with the GET verb')
        return render(request, 'paws/f_saint2year.html', context)
    if request.method == "POST":
        # all the information entered in the form is now accessible in the form
        # of a dictionary
        # <QueryDict: {'hostname': ['h'], 'csrfmiddlewaretoken': ['gyToMKbADq4PZfeMopGZOhYP8iawGGzhpmk5XglO0hIrW8tAECggLLzUsFyhIB5h']}>
        form_data = request.POST

        context = {'page_title': "Saint to Year, Output"}
        context['page_summary_text'] = "Outcome of: 'Tell me birth year of " + form_data['field_in']

        context['field_in'] = form_data['field_in']

        from paws.libs.labs import one2one
        year = one2one.saint2year(form_data['field_in'])
        context['field_out'] = year

        return render(request, 'paws/r_one2one.html', context)



def year2city(request):
    if request.method == "GET":
        context = {'page_title': "Year to City, Input"}
        context['page_summary_text'] = "This is what I do: You give me a Year and I will give you what sport games took place there."
        logger.debug('DEBUB Got a request for year2city view with the GET verb')
        return render(request, 'paws/f_year2city.html', context)
    if request.method == "POST":
        # all the information entered in the form is now accessible in the form
        # of a dictionary
        # <QueryDict: {'hostname': ['h'], 'csrfmiddlewaretoken': ['gyToMKbADq4PZfeMopGZOhYP8iawGGzhpmk5XglO0hIrW8tAECggLLzUsFyhIB5h']}>
        form_data = request.POST
        context = {'page_title': "Year to City, Output"}
        context['page_summary_text'] = "Outcome of: 'Tell me a Year' and I will tell you what sport games took place there.'"
        context['field_in'] = form_data['field_in']

        from paws.libs.labs import one2one
        year = one2one.year2city(form_data['field_in'])
        context['field_out'] = year

        return render(request, 'paws/r_one2one.html', context)

