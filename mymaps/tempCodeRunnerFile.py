    ward = request.POST.get('ward')
            pct = request.POST.get('pct')
            print(f'Ward: {ward}')
            print(f'PCT: {pct}')
            # Perform further processing with the ward and pct values
            
            # Return a JSON response if needed
            data = {
                'ward': ward,
                'pct': pct
            }
            return JsonResponse(data)