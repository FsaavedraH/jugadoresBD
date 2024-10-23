import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Player, Team

@csrf_exempt
def api_root(request):
    return JsonResponse({
        'players': '/api/players/',
        'teams': '/api/teams/',
        'transfers': '/api/transfers/',
    })

@csrf_exempt
def player_view(request, player_id=None):
    if request.method == 'GET':
        if player_id:
            try:
                player = Player.objects.get(id=player_id)
                return JsonResponse(player.to_dict())
            except Player.DoesNotExist:
                return JsonResponse({'error': 'Player not found'}, status=404)
        else:
            players = Player.objects.all()
            return JsonResponse([player.to_dict() for player in players], safe=False)

    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
            player = Player(**data)
            player.save()
            return JsonResponse(player.to_dict(), status=201)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

    elif request.method == 'PUT':
        if not player_id:
            return JsonResponse({'error': 'Player ID required'}, status=400)

        data = json.loads(request.body)
        try:
            player = Player.objects.get(id=player_id)
            for key, value in data.items():
                setattr(player, key, value)
            player.save()
            return JsonResponse(player.to_dict())
        except Player.DoesNotExist:
            return JsonResponse({'error': 'Player not found'}, status=404)

    elif request.method == 'DELETE':
        if not player_id:
            return JsonResponse({'error': 'Player ID required'}, status=400)

        try:
            player = Player.objects.get(id=player_id)
            player.delete()
            return JsonResponse({'message': 'Player deleted'}, status=204)
        except Player.DoesNotExist:
            return JsonResponse({'error': 'Player not found'}, status=404)

@csrf_exempt
def team_view(request, team_id=None):
    if request.method == 'GET':
        if team_id:
            try:
                team = Team.objects.get(id=team_id)
                return JsonResponse(team.to_dict())
            except Team.DoesNotExist:
                return JsonResponse({'error': 'Team not found'}, status=404)
        else:
            teams = Team.objects.all()
            return JsonResponse([team.to_dict() for team in teams], safe=False)

    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
            team = Team(
                name_team=data.get("name_team"),
                country=data.get("country")
            )
            team.save()
            return JsonResponse(team.to_dict(), status=201)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

    elif request.method == 'PUT':
        if not team_id:
            return JsonResponse({'error': 'Team ID required'}, status=400)

        data = json.loads(request.body)
        try:
            team = Team.objects.get(id=team_id)
            for key, value in data.items():
                setattr(team, key, value)
            team.save()
            return JsonResponse(team.to_dict())
        except Team.DoesNotExist:
            return JsonResponse({'error': 'Team not found'}, status=404)

    elif request.method == 'DELETE':
        if not team_id:
            return JsonResponse({'error': 'Team ID required'}, status=400)

        try:
            team = Team.objects.get(id=team_id)
            team.delete()
            return JsonResponse({'message': 'Team deleted'}, status=204)
        except Team.DoesNotExist:
            return JsonResponse({'error': 'Team not found'}, status=404)
